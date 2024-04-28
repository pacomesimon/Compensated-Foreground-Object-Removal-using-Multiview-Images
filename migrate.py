import os

folders_to_create = [
    "DATA/original_images",
    "INFERENCE_DATA",
    "LABELS/masks_imgs",
    "LABELS/model_outputs",
    "MODEL_CHECKPOINTS",
    "STITCHED_IMAGES"
]

for folder in folders_to_create:
    os.makedirs(folder, exist_ok=True)
