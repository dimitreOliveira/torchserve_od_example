import requests
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def make_request(url, image_path):
    img_file = open(image_path, 'rb')
    response = requests.post(url, data=img_file.read())
    return response.json()

def load_image(image_path) :
    img = Image.open(image_path)
    img.load()
    img = np.array(img, dtype=np.uint8)
    return img

def visualize_detections(image_path, detections, figsize=(7, 7)):
    img = load_image(image_path)
    plt.figure(figsize=figsize)
    plt.axis("off")
    plt.imshow(img)

    for detection in detections:
        score = detection['score']
        name = [x for x in detection.keys() if x != 'score'][0]
        box = detection[name]
        
        ax = plt.gca()
        text = "{}: {:.2f}".format(name, score)
        x1, y1, x2, y2 = box
        w, h = x2 - x1, y2 - y1
        patch = plt.Rectangle(
            [x1, y1], w, h, fill=False, edgecolor='r', linewidth=3
        )
        ax.add_patch(patch)
        ax.text(
            x1,
            y1,
            text,
            bbox={"facecolor": 'r', "alpha": 0.4},
            clip_box=ax.clipbox,
            clip_on=True,
        )
    plt.show()
