import yfinance as yf

def get_data(ticker, period, start, end):
    tickerData = yf.Ticker(ticker)
    tickerDf = tickerData.history(period=period, start=start, end=end)
    tickerDf = tickerDf[['Close']]

    return tickerDf
    
get_data('CSCO', '1d', '2010-01-01', '2020-01-25')