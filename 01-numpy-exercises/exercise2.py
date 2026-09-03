import numpy as np

matrix = np.arange(1,10).reshape(3,3)

print("==========")

row_sum = matrix.sum(axis=1)
print(f"row_sum: {row_sum}")
print("==========")
col_sum = matrix.sum(axis=0)
print(f"col_sum: {col_sum}")
print("==========")
print(f"matrix[1,1]: {matrix[1,1]}")
print("==========")
print(f"matrix*2:\n{matrix * 2}")