import argparse
from graph import find_max_city, graph_stonk


# sample input: find_max_city('MAR', '1d', '2020-10-01', '2020-12-31', 0.8)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--predict", nargs=5, type=str, help="ticker, period, start date, end date, percent of skyline to use")
    parser.add_argument("--analyze", nargs=6, type=str, help="city, ticker, period, start date, end date, percent of skyline to use")

    opt = parser.parse_args()

    if opt.predict:
        find_max_city(opt.predict[0], opt.predict[1], opt.predict[2], opt.predict[3], float(opt.predict[4]))

    if opt.analyze:
        graph_stonk(opt.analyze[0], opt.analyze[1], opt.analyze[2], opt.analyze[3], opt.analyze[4], float(opt.analyze[5]))