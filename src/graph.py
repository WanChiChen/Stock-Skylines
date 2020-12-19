import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageOps
from otsu import run
from stonk import get_data

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
    plt.close()

    return graph

def graph_stonk(ticker, period, start, end):
    data = get_data(ticker, period, start, end)
    index = data.index

    city = graph("shanghai.jpg")
    diff = len(index) - len(city)
    length_scale = len(index) / len(city)
    city = np.append(city, np.zeros(diff))

    value_scale = np.median(city) / data['Close'].median()
    for i in np.arange(len(city)):
        city[i] /= value_scale

    city = pd.DataFrame(data=city, columns=['City'], index=index)
    data = data.join(city)

    data.plot()
    plt.ylim(0, 50)
    plt.show()

graph_stonk('AAPL', '1d', '2010-01-01', '2020-01-25')