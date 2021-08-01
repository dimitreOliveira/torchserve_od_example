## Simple example of using TorchServe to serve a PyTorch Object Detection model


### Steps to use:

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

### Content

- models: ...
- samples: ...
- scripts: ...
- utils: ...