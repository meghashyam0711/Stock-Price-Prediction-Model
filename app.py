import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Stock Price Prediction")

tickers = ["AMZN", "MSFT", "GOOGL", "AAPL"]
ticker = st.selectbox("Select stock", tickers)
df = pd.read_csv(f"{ticker}_features.csv", index_col=0, parse_dates=True)
st.line_chart(df[['Close', 'MA_5', 'MA_10']])
