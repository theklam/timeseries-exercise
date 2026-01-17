import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('store-sales-time-series-forecasting/transactions.csv')
df['date'] = pd.to_datetime(df['date'])
print("Number of rows and columns:", df.shape)
print("Types of each column:\n", df.dtypes)
print(df.head())

# first, filter for the last year of data
latest_date = df['date'].max()
one_year_ago = latest_date - pd.DateOffset(years=1)
df = df[df['date'] >= one_year_ago]
print("Number of rows and columns after filtering for last year:", df.shape)
print(df.head())

# next, filter for a specific store, e.g., store number 1
store_1 = df[df['store_nbr'] == 1] 
print("Number of rows and columns:", store_1.shape)
print(store_1.head())

store_2 = df[df['store_nbr'] == 2] 
print("Number of rows and columns:", store_2.shape)
print(store_2.head())

plt.plot(store_1['date'], store_1['transactions'], label='Store 1')
plt.plot(store_2['date'], store_2['transactions'], label='Store 2')
plt.xlabel('Date')
plt.ylabel('Number of Transactions')
plt.title('Store 1 vs Store 2 Transactions (Past Year)')
plt.legend()

plt.show()
