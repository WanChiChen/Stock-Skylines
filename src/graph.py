import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageOps
from otsu import run
from stonk import get_data

def graph(src):
    run(src)
    img = Image.open(f"../segmented/{src}")
    img = ImageOps.grayscale(img)
    img = np.asarray(img)
    rows, cols = img.shape
    graph_img = np.zeros((rows, cols))
    graph = np.zeros(cols)

    print("Graphing City...")

    for j in np.arange(cols):
        for i in np.arange(rows):
            if img[i, j] == 0:
                graph_img[i, j] = 255
                graph[j] = rows - i
                break

    np.savetxt(f"../graphs/charts/{src}.tsv", graph, delimiter="\t")

    plt.plot(np.arange(cols), graph)
    plt.savefig(f"../graphs/images/{src}")
    plt.close()

    return graph

def get_similarity(data1, data2):
    length = min(len(data1), len(data2))

    percents = np.zeros(length)
    for i in np.arange(length):
        percents[i] = 100 * np.absolute((data1[i] - data2[i])) / data1[i]

    return 100 - np.mean(percents)

def graph_stonk(city, ticker, period, start, end):
    data = get_data(ticker, period, start, end)
    date_index = data.index

    city_graph = graph(f"{city}.jpg")
    length_scale = (len(date_index) / len(city_graph))

    print("Graphing Stock...")

    data = data.reset_index()

    if length_scale > 1:
        length_scale = np.ceil(length_scale)
        data = data[data.index % length_scale == 0]
        data = data.reset_index()
        data = data.drop('index', axis=1)

    if length_scale < 1:
        length_scale = ( 1 / length_scale)
        length_scale = int(np.ceil(length_scale))
        indicies = np.arange(0, city_graph.size, length_scale, dtype='int64')
        city_graph = np.take(city_graph, indicies)

    value_scale = np.median(city_graph) / data['Close'].median()
    for i in np.arange(len(city_graph)):
        city_graph[i] /= value_scale

    city_graph = pd.DataFrame(data=city_graph, columns=[city])
    data = data.join(city_graph)
    data = data.dropna()

    similarity = get_similarity(data['Close'].to_numpy(), data[city].to_numpy())
    print(f"{city} and {ticker} are {similarity} percent similar")

    data = data.set_index('Date')
    data = data.rename(columns={"Close" : ticker})

    data.plot()
    plt.show()

graph_stonk('Singapore', 'MAR', '1d', '2020-03-01', '2020-08-24')