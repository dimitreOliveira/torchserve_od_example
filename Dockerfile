FROM pytorch/torchserve:latest

COPY ./utils utils

COPY ./models models

COPY ./scripts scripts