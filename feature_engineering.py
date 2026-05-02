import pandas as pd

tickers = ["AMZN", "MSFT", "GOOGL", "AAPL"]

for ticker in tickers:
    df = pd.read_csv(f"{ticker}_data.csv", index_col=0, parse_dates=True)
    df['MA_5'] = df['Close'].rolling(window=5).mean()
    df['MA_10'] = df['Close'].rolling(window=10).mean()
    df.to_csv(f"{ticker}_features.csv")
    print(f"{ticker}_features.csv created.")
