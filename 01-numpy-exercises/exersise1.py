import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
average = arr.mean()
total_sum = arr.sum()
print("=============")
print(f"average: {average}")
print("=============")
print(f"sum: {total_sum}")
print("=============")
print(f" arr+10:\n{arr + 5}")
print("=============")
print(f" arr > 10:\n{arr[arr >10]}")

