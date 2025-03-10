#Stock Market Data Analysis
#This will help you practice data fetching, cleaning, visualization, and basic analysis with Pandas and Matplotlib

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define stock symbol and time period
stock_symbol = "AAPL"
stock_data = yf.download(stock_symbol, period="6mo")

# Display first few rows
print(stock_data.head())

#Plot Stock Closing Price Trend
# plt.figure(figsize=(12,5))
# plt.plot(stock_data.index, stock_data["Close"],label=f"{stock_symbol} Closing Price",color='blue')
# plt.xlabel("Date")
# plt.ylabel("Closing Price (USD)")
# plt.title(f"{stock_symbol} Stock Price Trend")
# plt.legend() #label given in 'plot' won't come without this
# plt.grid()
# plt.show()

#Moving Average Calculation
# stock_data["50_MA"]=stock_data["Close"].rolling(window=50).mean()
# plt.figure(figsize=(12,5))
# plt.plot(stock_data.index, stock_data["Close"],label=f"{stock_symbol} Closing Price",color='blue')
# plt.plot(stock_data.index, stock_data["50_MA"],label="50 Day MA",color='red')
# plt.xlabel("Date")
# plt.ylabel("Price (USD)")
# plt.title(f"{stock_symbol} Stock Price with 50-Day Moving Average")
# plt.legend()
# plt.grid()
# plt.show()

#Daily Returns Calculation as percentage
stock_data["Daily Return"]=stock_data["Close"].pct_change()
sns.histplot(stock_data["Daily Return"].dropna(), bins=50, kde=True)
plt.title(f"{stock_symbol} Daily Returns Distribution")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.show()

#Save and Analyze Data
stock_data.to_csv(f"{stock_symbol}_stock_data.csv")