FROM pytorch/torchserve:latest

EXPOSE 8080

COPY ./models models

COPY ./scripts scripts

COPY ./utils utils