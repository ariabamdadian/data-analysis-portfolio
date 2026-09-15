import pandas as pd

df = pd.read_csv('people.csv')

print("Age > 30:")
print(df[df['age'] > 30])

print("\nCity == Tehran:")
print(df[df['city'] == 'Tehran'])

print("\nAge > 30 AND City == Tehran:")
print(df[(df['age'] > 30) & (df['city'] == 'Tehran')])

print("\nCount of age > 30:")
print(len(df[df['age'] > 30]))