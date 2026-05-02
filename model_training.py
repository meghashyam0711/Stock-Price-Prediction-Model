import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

tickers = ["AMZN", "MSFT", "GOOGL", "AAPL"]

for ticker in tickers:
    df = pd.read_csv(f"{ticker}_features.csv", index_col=0, parse_dates=True).dropna()
    X = df[['MA_5', 'MA_10']]
    y = df['Close']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False)

    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)

    poly = PolynomialFeatures(degree=2)
    X_poly_train = poly.fit_transform(X_train)
    X_poly_test = poly.transform(X_test)
    pr = LinearRegression()
    pr.fit(X_poly_train, y_train)
    y_pred_pr = pr.predict(X_poly_test)

    svr = SVR(kernel='rbf')
    svr.fit(X_train, y_train)
    y_pred_svr = svr.predict(X_test)

    print(f"\nResults for {ticker}:")
    for model_name, y_pred in zip(["Linear Regression", "Polynomial Regression", "SVR"],
                                  [y_pred_lr, y_pred_pr, y_pred_svr]):
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print(f"{model_name}: MSE={mse:.3f}, MAE={mae:.3f}, R²={r2:.3f}")
    print()
