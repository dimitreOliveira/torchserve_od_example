FROM pytorch/torchserve:latest

COPY ./models models

COPY ./scripts scripts

COPY ./utils utils