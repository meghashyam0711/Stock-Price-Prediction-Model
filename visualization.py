import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

tickers = ["AMZN", "MSFT", "GOOGL", "AAPL"]

for ticker in tickers:
    df = pd.read_csv(f"{ticker}_features.csv", index_col=0, parse_dates=True).dropna()
    X = df[['MA_5', 'MA_10']]
    y = df['Close']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False)

    lr = LinearRegression().fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)

    plt.figure(figsize=(12, 6))
    plt.plot(y_test.index, y_test, label='Actual Price')
    plt.plot(y_test.index, y_pred_lr, label='Linear Regression Predicted')
    plt.title(f'Actual vs Predicted Closing Price: {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
