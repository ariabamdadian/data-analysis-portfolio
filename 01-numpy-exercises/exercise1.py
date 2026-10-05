import numpy as np

arr = np.arange(1, 21)

print(f"Average: {arr.mean()}")
print(f"Sum: {arr.sum()}")
print(f"arr + 5:\n{arr + 5}")
print(f"arr > 10:\n{arr[arr > 10]}")