import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['Ali', 'Sara', 'Reza', 'Maryam', 'Hossein'],
    'age': [25, 30, np.nan, 28, 100],
    'city': ['Tehran', 'Shiraz', 'Tehran', np.nan, 'Isfahan']
})

print("Original DataFrame:")
print(df)

print("\nAfter dropna:")
print(df.dropna())

print("\nAfter fillna:")
print(df.fillna('Unknown'))

print("\nAfter removing outliers (age < 100):")
print(df[df['age'] < 100])