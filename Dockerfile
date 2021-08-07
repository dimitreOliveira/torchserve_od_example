FROM pytorch/torchserve:latest
COPY ./utils utils
COPY ./scripts scripts
USER root
RUN ["chmod", "+x", "./scripts/archive_model.sh"]
RUN ["chmod", "+x", "./scripts/start_torchserve.sh"]