import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
from otsu import run

def graph(src):
    img = Image.open(f"../segmented/{src}")
    img = ImageOps.grayscale(img)
    img = np.asarray(img)
    rows, cols = img.shape
    graph_img = np.zeros((rows, cols))
    graph = np.zeros(cols)

    for j in np.arange(cols):
        for i in np.arange(rows):
            if img[i, j] == 0:
                graph_img[i, j] = 255
                graph[j] = rows - i
                break

    plt.plot(np.arange(cols), graph)
    plt.ylim(0, 700)
    img = Image.fromarray(graph_img)
    img.convert("L").save(f"../graphs/images/{src}")
    plt.savefig(f"../graphs/charts/{src}")

graph("shanghai.jpg")