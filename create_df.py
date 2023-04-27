import pandas as pd

print("creating the dataframe from data.csv file..")
df = pd.read_csv('data.csv', sep=',', names=['movie', 'user','rating','date'])
df.date = pd.to_datetime(df.date)
print('Done.\n')

# we are arranging the ratings according to users.
print('Sorting the dataframe by user..')
df.sort_values(by='user', inplace=True)
print('Done..')

print(df.head())