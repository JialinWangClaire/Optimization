from create_df import df
import pandas as pd

df = df.head(20000)
two_level_index_series = df.set_index(['movie','user'])['rating']
new_df = two_level_index_series.unstack(level=0)
df = new_df.dropna(axis=1, how='all')
percent_na = df.isna().sum() / len(df)
df = df.dropna(axis=1, thresh=len(df)*0.2)
df.to_pickle('dataframe.pkl')