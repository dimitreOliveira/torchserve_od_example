# Simple example of using TorchServe to serve a PyTorch Object Detection model


# Content
- [Local Setup](#local-setup)
- [Docker Setup](#docker-setup)
- [Run locally](#run-locally)
- [Run with Docker](#run-with-docker)
- [Content](#content)
- [References](#references)


## Local Setup
> Optional

## Docker Setup


## Run locally
**Download FastRCNN model weights**
```bash
sh scripts/get_fastrcnn.sh
```

**Archive model**
```bash
sh scripts/archive_model.sh
```

**Start TorchServe**
```bash
sh scripts/start_torchserve.sh
```

**Run sample inference using REST APIs**
```bash
curl http://127.0.0.1:8080/predictions/densenet161 -T ./samples/man.jpg
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
sudo docker run -p 8080:8080 -u 0 -ti docker_torchserve /bin/bash
```

**Download FastRCNN model weights**
> Don't needed if the model weights is already downloaded at "models" folder
```bash
sh scripts/get_fastrcnn.sh
```

**Archive model**
```bash
sh scripts/archive_model.sh
```

**Start TorchServe**
```bash
sh scripts/start_torchserve.sh
```


## Content
- models: ...
- samples: ...
- scripts: ...
- utils: ...


## References
- [PytorchServe](https://github.com/pytorch/serve)
- [PytorchServe - FastRCNN example](https://github.com/pytorch/serve/tree/master/examples/object_detector/fast-rcnn)
- [PytorchServe - Docker](https://github.com/pytorch/serve/tree/master/docker)
- [Docker - run](https://docs.docker.com/engine/reference/commandline/run/)