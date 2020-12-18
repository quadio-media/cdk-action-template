FROM quadiomedia/giles:1.0.0

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
        build-essential

COPY ./requirements.txt /home/requirements.txt
RUN pip install --upgrade pip \
    && pip install --use-feature=2020-resolver --no-cache-dir -r /home/requirements.txt \
    && rm /home/requirements.txt
# Clean up
RUN apt-get remove -y --purge build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*