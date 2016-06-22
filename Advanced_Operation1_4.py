#Resampling ohlc

import pandas as pd
import urllib.request
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

df = pd.read_pickle('df.pickle')
df.sort_values('Date', inplace = True)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace = True)

print(df.head())

df2 = df['Adjusted Close'].resample('2D', how='ohlc', fill_method = 'ffill')

print(df2.head())

#df2.dropna(inplace=True)


if df2.isnull().values.sum() > 1:
    print('We contain NAN data!')
