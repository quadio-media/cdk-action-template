# Provision AWS VPC

This action provisions an AWS VPC using the AWS CDK cli. The intention is to encapsulate
the code needed to provision resources. The goal is to avoid conflating microservice application code
with "infrastructure as code". As such all infrastructure code lives in the [aws](aws) package where the
docker entrypoint is `cdk --app aws/app.py $*`

## Inputs

### `subcommand`

**Optional** The aws-cdk subcommand to run. Default `"deploy -f"`.

## Example usage

```yaml
uses: quadio-media/provision-aws-vpc@v1
with:
  subcommand: deploy -f
env:
  AWS_REGION: us-east-1
  AWS_ACCOUNT_ID: ${{ secrets.AWS_ACCOUNT_ID }}
  AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
  AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
  EXPORT_NAME: CFN_VPC_ID
  STACK_NAME: MyVpc
```

### Configuration

The following settings must be passed as environment variables as shown in the example. Sensitive information, especially `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`, should be [set as encrypted secrets](https://help.github.com/en/articles/virtual-environments-for-github-actions#creating-and-using-secrets-encrypted-variables) — otherwise, they'll be public to anyone browsing your repository's source code and CI logs.

| Key | Value | Suggested Type | Required | Default |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| `AWS_ACCOUNT_ID` | Your AWS Account ID. | `secret env` | **Yes** | N/A |
| `AWS_ACCESS_KEY_ID` | Your AWS Access Key. [More info here.](https://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html) | `secret env` | **Yes** | N/A |
| `AWS_SECRET_ACCESS_KEY` | Your AWS Secret Access Key. [More info here.](https://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html) | `secret env` | **Yes** | N/A |
| `AWS_REGION` | The region you want the VPC Stack to live in. | `env` | **Yes** | N/A |
| `CIDR` | The CIDR you want to use for your virtual network. | `env` | No | `10.12.0.0/16` |
| `EXPORT_NAME` | The variable name you want to use to export your VPCs ID. | `env` | No | `VpcId` |
| `STACK_NAME` | The name you want to use for your VPC stack. | `env` | No | `Vpc` |


## License

This project is distributed under the [MIT license](LICENSE).
