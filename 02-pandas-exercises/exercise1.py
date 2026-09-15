import pandas as pd

df = pd.read_csv("people.csv")

print("First 5 rows:")
print(df.head(5))

print("\nLast 5 rows:")
print(df.tail(5))

print("\nInfo:")
print(df.info())

print("\nDescribe:")
print(df.describe())