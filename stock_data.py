import yfinance as yf

tickers = ["AMZN", "MSFT", "GOOGL", "AAPL"]

for ticker in tickers:
    stock = yf.Ticker(ticker)
    df = stock.history(period="5y")
    df.to_csv(f"{ticker}_data.csv")
    print(f"{ticker}_data.csv saved.")
