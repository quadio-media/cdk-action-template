#!/usr/bin/env python3

import environs
from aws_cdk import (
    core,
    aws_ec2 as ec2,
)


_env = environs.Env()
AWS_ACCOUNT_ID = _env('AWS_ACCOUNT_ID')
AWS_REGION = _env('AWS_REGION')
AWS_ACCESS_KEY_ID = _env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = _env('AWS_SECRET_ACCESS_KEY')
CIDR = _env('CIDR', default='10.12.0.0/16')
EXPORT_NAME = _env('EXPORT_NAME', default='VpcId')
STACK_NAME = _env('STACK_NAME', default='Vpc')


class VpcStack(core.Stack):

    def __init__(
        self,
        scope: core.Construct,
        id: str,
        env: core.Environment,
        **kwargs
    ):
        super().__init__(scope, id, env=env, **kwargs)

        subnet0 = ec2.SubnetConfiguration(
            name='Public',
            subnet_type=ec2.SubnetType.PUBLIC,
            cidr_mask=24
        )
        subnet1 = ec2.SubnetConfiguration(
            name='Private',
            subnet_type=ec2.SubnetType.PRIVATE,
            cidr_mask=24
        )

        vpc = ec2.Vpc(
            self,
            'VPC',
            cidr=CIDR,
            enable_dns_hostnames=True,
            enable_dns_support=True,
            nat_gateways=1,
            subnet_configuration=[
                subnet0,
                subnet1,
            ]
        )
        # Usage: core.Fn.import_value('VpcId')
        core.CfnOutput(self, "VpcId", value=vpc.vpc_id, export_name=EXPORT_NAME)


env = core.Environment(account=AWS_ACCOUNT_ID, region=AWS_REGION)
app = core.App()
main = VpcStack(app, STACK_NAME, env=env)
app.synth()
