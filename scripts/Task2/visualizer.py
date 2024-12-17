# visualize.py
import matplotlib.pyplot as plt
import mplfinance as mpf

def plot_stock_data(stock_data):
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data['Close'], label='Close Price', color='blue')
    plt.plot(stock_data['SMA_20'], label='20-Day SMA', color='orange')
    plt.title('Stock Price and Indicators')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def plot_volume(stock_data):
    plt.figure(figsize=(12, 4))
    plt.bar(stock_data['Date'], stock_data['Volume'], color='gray', alpha=0.5)
    plt.title('Trading Volume')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_rsi(stock_data):
    plt.figure(figsize=(12, 4))
    plt.plot(stock_data['Date'], stock_data['RSI'], label='RSI', color='purple')
    plt.axhline(70, linestyle='--', alpha=0.5, color='red')
    plt.axhline(30, linestyle='--', alpha=0.5, color='green')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()

def plot_macd(stock_data):
    plt.figure(figsize=(12, 4))
    plt.plot(stock_data['Date'], stock_data['MACD'], label='MACD', color='blue')
    plt.plot(stock_data['Date'], stock_data['MACD_signal'], label='MACD Signal', color='orange')
    plt.title('Moving Average Convergence Divergence (MACD)')
    plt.xlabel('Date')
    plt.ylabel('MACD')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()