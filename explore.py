import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('store-sales-time-series-forecasting/transactions.csv')
print(df.head())

plt.plot(df['date'], df['transactions'])
plt.xlabel('Date')
plt.ylabel('Number of Transactions')
plt.title('Store Transactions Over Time')

plt.show()
