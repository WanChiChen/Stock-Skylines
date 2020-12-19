import numpy as np
from PIL import Image, ImageOps
from otsu import run

def graph(src):
    img = Image.open(f"../segmented/{src}")
    img = ImageOps.grayscale(img)
    img = np.asarray(img)
    rows, cols = img.shape
    graph_img = np.zeros((rows, cols))

    for j in np.arange(cols):
        for i in np.arange(rows):
            if img[i, j] == 0:
                graph_img[i, j] = 255
                break
    img = Image.fromarray(graph_img)
    img.convert("L").save(f"../graphs/{src}")

run("shanghai.jpg")
graph("shanghai.jpg")