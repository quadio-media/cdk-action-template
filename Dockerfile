FROM quadiomedia/CHANGE_ME:1.0.0

RUN mkdir -p /home/actions
COPY ./aws /home/actions/aws
COPY ./bin /home/actions/bin

ENV PYTHONPATH "${PYTHONPATH}:/home/actions"
ENV PATH "${PATH}:/home/actions/bin"

RUN mkdir -p /home/src
WORKDIR /home/src

ENTRYPOINT ["entrypoint.sh"]
