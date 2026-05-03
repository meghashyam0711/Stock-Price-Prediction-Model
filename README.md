# Stock Price Prediction

A comprehensive machine learning project to analyze and predict stock prices using historical data and technical indicators. This project leverages multiple regression models to forecast the closing prices of major tech stocks (AMZN, MSFT, GOOGL, AAPL).

##  Features

- **Automated Data Retrieval**: Fetches 5 years of historical stock data using `yfinance`.
- **Feature Engineering**: Calculates technical indicators like 5-day and 10-day Moving Averages (MA_5, MA_10).
- **Multiple ML Models**: Implements and compares:
  - Linear Regression
  - Polynomial Regression (Degree 2)
  - Support Vector Regression (SVR)
- **Performance Evaluation**: Provides metrics such as Mean Squared Error (MSE), Mean Absolute Error (MAE), and R² Score.
- **Interactive Dashboard**: A Streamlit-based web interface to visualize historical prices and moving averages.
- **Data Visualization**: Standalone scripts for plotting actual vs. predicted prices.

##  Tech Stack

- **Language**: Python
- **Libraries**:
  - `yfinance`: For fetching market data.
  - `pandas`: For data manipulation and analysis.
  - `scikit-learn`: For building and evaluating machine learning models.
  - `matplotlib`: For creating static visualizations.
  - `streamlit`: For building the interactive web application.

##  Project Structure

```text
StockPricePrediction/
├── app.py                  # Main Streamlit dashboard
├── stock_data.py           # Script to fetch historical data
├── feature_engineering.py   # Script to calculate technical indicators
├── model_training.py       # Script to train and evaluate models
├── visualization.py        # Standalone visualization script
├── *_data.csv              # Raw historical data (generated)
├── *_features.csv          # Data with engineered features (generated)
└── venv/                   # Virtual environment
```

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/meghashyam0711/Stock-Price-Prediction-Model.git
   cd Stock-Price-Prediction-Model
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install yfinance pandas scikit-learn matplotlib streamlit
   ```

## Usage

### 1. Data Collection
Fetch the latest historical data:
```bash
python stock_data.py
```

### 2. Feature Engineering
Process the raw data to generate indicators:
```bash
python feature_engineering.py
```

### 3. Model Training
Train models and see evaluation results:
```bash
python model_training.py
```

### 4. Visualization
Run the interactive dashboard:
```bash
streamlit run app.py
```
Or run the standalone visualization script:
```bash
python visualization.py
```

##  Results

The models are evaluated based on their ability to predict the closing price using moving averages. Example output:

| Model | MSE | MAE | R² |
|-------|-----|-----|----|
| Linear Regression | ... | ... | ... |
| SVR | ... | ... | ... |

##  Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---
*Created with  for SEM 3 Mini Project.*
