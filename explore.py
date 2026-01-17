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

latest_date = df['date'].max()
one_year_ago = latest_date - pd.DateOffset(years=1)
df = df[df['date'] >= one_year_ago]
print("Number of rows and columns after filtering for last year:", df.shape)
print(df.head())

# after filtering for store 1 and last year, we check for missing dates
all_dates = pd.date_range(start=one_year_ago, end=latest_date)
missing_dates = all_dates.difference(df['date'])
print("start date:", one_year_ago)
print("end date:", latest_date)
print("Missing dates:", missing_dates)

df['transactions_7d_avg'] = df['transactions'].rolling(window=7).mean()

plt.plot(df['date'], df['transactions'], label='Daily')
plt.plot(df['date'], df['transactions_7d_avg'], label='7-day Average')
plt.xlabel('Date')
plt.ylabel('Number of Transactions')
plt.title('Store 1 Transactions (Past Year)')

plt.show()
