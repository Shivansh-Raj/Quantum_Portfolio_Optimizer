import yfinance as yf
import pandas as pd

def fetch_data(tickers):
    data = yf.download(tickers=tickers, period = "1y")["Close"]
    # data = yf.download(tickers=tickers, period = "1y")["Adj Close"]
    returns = data.pct_change().dropna()

    mu = returns.mean()
    cov = returns.cov()

    return mu, cov