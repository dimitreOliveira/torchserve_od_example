from torchvision.models.detection.faster_rcnn import FasterRCNN
from torchvision.models.detection.backbone_utils import resnet_fpn_backbone


class FRCNNObjectDetector(FasterRCNN):
    def __init__(self, num_classes=91, **kwargs):
        backbone = resnet_fpn_backbone(backbone_name='resnet50', pretrained=False)
        super(FRCNNObjectDetector, self).__init__(backbone, num_classes, **kwargs)