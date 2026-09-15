import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Ali', 'Sara', 'Reza', 'Maryam'],
    'age': [25, 30, 35, 28]
})

df2 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'job': ['Engineer', 'Doctor', 'Teacher', 'Designer'],
    'salary': [5000, 7000, 4000, 6000]
})

merged = pd.merge(df1, df2, on='id')

print("Merged DataFrame:")
print(merged)