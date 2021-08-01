torch-model-archiver --model-name resnet18 \
--version 1.0  \
--serialized-file ./models/resnet18.pt \
--export-path model_store \
--extra-files ./index_to_name.json \
--handler image_classifier -f
