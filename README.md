# Simple example of using TorchServe to serve a PyTorch Object Detection model


# Repository content
- [Local Setup](#local-setup)
- [Docker Setup](#docker-setup)
- [General Setup](#general-setup)
- [Run locally](#run-locally)
- [Run with Docker](#run-with-docker)
- [Run with Docker compose](#run-with-docker-compose)
- [Content](#content)
- [Inference](#inference)
- [References](#references)


## Local Setup
> Optional
- PyTorch - Refer to the [official PyTorch installation guide](https://pytorch.org/get-started/locally/#linux-installation)
- Torchserve - Refer to the [official Torchserve installation guide](https://github.com/pytorch/serve#install-torchserve-and-torch-model-archiver)


## Docker Setup
- Docker - Refer to the [official docker installation guide](https://help.github.com/en/github/getting-started-with-github/set-up-git)


## General Setup
**Download FastRCNN model weights**
```bash
sh scripts/get_fastrcnn.sh
```


## Run locally
**Archive model**
```bash
sh scripts/archive_model.sh
```

**Start TorchServe**
```bash
sh scripts/start_torchserve.sh
```

**Stop TorchServe**
```bash
torchserve --stop
```


## Run with Docker
**Build Docker image from the Dockerfile**
```bash
sudo docker build -f Dockerfile -t docker_torchserve .
```

**Run the Docker container**
```bash
sudo docker run -p 8080:8080 -u 0 -ti -v $(pwd)/models/:/home/model-server/models/ docker_torchserve /bin/bash
```

**Archive model**
```bash
sh scripts/archive_model.sh
```

**Start TorchServe**
```bash
sh scripts/start_torchserve.sh
```

**Stop TorchServe**
```bash
torchserve --stop
```


## Run with Docker compose
**Build image and run with Build and run your app with Docker compose**
```bash
sudo docker-compose up
```

**Stop the application**
```bash
docker-compose down
```


## Inference
**Run sample inference using REST APIs**
```bash
curl http://127.0.0.1:8080/predictions/fastrcnn -T ./samples/man2.jpg
```

**Or iteratively run the "query_notebook.ipynb" notebook**


## Content
- models — Model's assets.
- samples — Image samples used to test inference.
- scripts — Scripts for general usage.
- utils — Utility files.
- query_notebook — Jupyter notebook for iterative inference.


## References
- [PytorchServe](https://github.com/pytorch/serve)
- [PytorchServe - FastRCNN example](https://github.com/pytorch/serve/tree/master/examples/object_detector/fast-rcnn)
- [PytorchServe - Docker](https://github.com/pytorch/serve/tree/master/docker)
- [Docker - run](https://docs.docker.com/engine/reference/commandline/run/)