import pandas as pd

df = pd.read_csv('02-pandas-exercises/people.csv')
print("First 2 rows:")
print(df.head(2))
print("\nLast 2 rows:")
print(df.tail(2))
print("\nInfo:")
print(df.info())
print("\nDescribe:")
print(df.describe())