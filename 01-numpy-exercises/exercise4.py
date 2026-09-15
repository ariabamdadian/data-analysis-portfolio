import numpy as np

tempratures = np.array([23,28,31,19,24,27,35,22,18,25])

average = tempratures.mean()
print(f"average: {average}\n")
count = 1
for day in tempratures:
    
    print(f"day {count}: {average - day}")
    count+=1
print(f"Hottest day: {tempratures.argmax()}\n")
print(f"Days > 25: {(tempratures > 25).sum()}\n")

new_tempratures = np.where(tempratures> 30, tempratures+2 , tempratures)
print(f"new_tempratures: {new_tempratures}")

    