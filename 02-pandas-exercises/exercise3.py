import pandas as pd

df = pd.read_csv('02-pandas-exercises/people.csv')

print("Mean age by city:")
print(df.groupby('city')['age'].mean())
print("\nCount by city:")
print(df.groupby('city')['age'].count())
print("\nSum age by city:")
print(df.groupby('city')['age'].sum())