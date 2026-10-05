import numpy as np

matrix = np.arange(1, 10).reshape(3, 3)

print(f"Row sums: {matrix.sum(axis=1)}")
print(f"Column sums: {matrix.sum(axis=0)}")
print(f"Middle element: {matrix[1, 1]}")
print(f"Matrix * 2:\n{matrix * 2}")