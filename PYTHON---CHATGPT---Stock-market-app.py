import yfinance as yf
import pandas as pd

# Function to fetch stock data
def get_stock_data(ticker):
    stock_data = yf.download(ticker, period="1y")  # Fetch 1 year of data
    return stock_data

# Function to calculate moving averages
def calculate_moving_averages(stock_data, short_window=20, long_window=50):
    stock_data['Short_MA'] = stock_data['Close'].rolling(window=short_window).mean()
    stock_data['Long_MA'] = stock_data['Close'].rolling(window=long_window).mean()
    return stock_data

# Function to generate buy/sell signals
def generate_signals(stock_data):
    stock_data['Signal'] = 0  # Default to 0 (Hold)
    stock_data['Signal'][stock_data['Short_MA'] > stock_data['Long_MA']] = 1  # Buy
    stock_data['Signal'][stock_data['Short_MA'] < stock_data['Long_MA']] = -1  # Sell
    return stock_data

# Function to print recommendation
def get_recommendation(stock_data):
    latest_signal = stock_data['Signal'].iloc[-1]
    if latest_signal == 1:
        return "BUY"
    elif latest_signal == -1:
        return "SELL"
    else:
        return "HOLD"

# Main function to run the app
def stock_market_app(ticker):
    stock_data = get_stock_data(ticker)
    stock_data = calculate_moving_averages(stock_data)
    stock_data = generate_signals(stock_data)
    recommendation = get_recommendation(stock_data)
    
    return f"The current recommendation for {ticker} is: {recommendation}"

# Example usage:
ticker = input("Enter stock ticker: ").upper()  # Example: AAPL for Apple Inc.
print(stock_market_app(ticker))
