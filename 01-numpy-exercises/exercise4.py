import numpy as np

temperatures = np.array([23, 28, 31, 19, 24, 27, 35, 22, 18, 25])

print(f"Average: {temperatures.mean()}")
print(f"Deviation from mean: {temperatures - temperatures.mean()}")
print(f"Hottest day index: {np.argmax(temperatures)}")
print(f"Days > 25: {(temperatures > 25).sum()}")
new_temps = np.where(temperatures > 30, temperatures + 2, temperatures)
print(f"New temperatures: {new_temps}")