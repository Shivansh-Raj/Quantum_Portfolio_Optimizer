import yfinance as yf
from qabo_transformer import qabo_transform
from qaoa_solver import qoao_implementation

tickers = ['AAPL', 'GOOGL', 'TSLA', 'MSFT']
data = yf.download(tickers,period="1y")

# Daily returns
returns = data.pct_change().dropna()
mu = returns.mean() * 252         # Expected return annualized
cov = returns.cov() * 252         # Covariance annualized

print(mu,"\n",cov)

qp = qabo_transform(tickers, mu, cov)
result = qoao_implementation(qp)

print(result)