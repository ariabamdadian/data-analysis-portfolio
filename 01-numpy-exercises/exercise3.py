import numpy as np

arr = np.random.randint(0,100 , size=10)

min_num = arr.min()
max_num = arr.max()

print(f"min num: {min_num}\n")

print(f"max num: {max_num}\n")
standard_deviation = np.std(arr)
print(f"standard deviation: {standard_deviation}\n")
print(f"20<arr<80: {arr[(arr>=20) & (arr<=80)]}\n")
print(((arr > 50).sum()/len(arr))*100)

