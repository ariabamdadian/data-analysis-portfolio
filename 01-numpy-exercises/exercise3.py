import numpy as np

arr = np.random.randint(0, 100, size=10)

print(f"Min: {arr.min()}")
print(f"Max: {arr.max()}")
print(f"Std: {np.std(arr)}")
print(f"Between 20-80: {arr[(arr >= 20) & (arr <= 80)]}")
print(f"Percentage > 50: {(arr > 50).sum() / len(arr) * 100}%")