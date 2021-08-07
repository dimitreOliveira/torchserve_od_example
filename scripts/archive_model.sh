torch-model-archiver --model-name fastrcnn \
--version 1.0 \
--serialized-file ./models/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth \
--model-file ./models/fastrcnn_model.py \
--extra-files ./utils/index_to_name.json \
--export-path ./model-store/ \
--handler object_detector -f