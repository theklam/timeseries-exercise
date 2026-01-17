import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('store-sales-time-series-forecasting/transactions.csv')
df['date'] = pd.to_datetime(df['date'])
print("Number of rows and columns:", df.shape)
print("Types of each column:\n", df.dtypes)
print(df.head())

df = df[df['store_nbr'] == 1] # filter for store 1
print("Number of rows and columns:", df.shape)
print(df.head())

plt.plot(df['date'], df['transactions'])
plt.xlabel('Date')
plt.ylabel('Number of Transactions')
plt.title('Store Transactions Over Time for Store 1')

plt.show()
