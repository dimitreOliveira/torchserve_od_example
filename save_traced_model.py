import torch
from torchvision import models

model = models.resnet18(pretrained=True)
model.eval()
example_input = torch.rand(1, 3, 224, 224)
traced_script_module = torch.jit.trace(model, example_input)
traced_script_module.save("models/resnet18.pt")
