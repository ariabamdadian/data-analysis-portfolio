import numpy as np

tempratures = np.array([23,28,31,19,24,27,35,22,18,25])

average = tempratures.mean()
print(f"average: {average}\n")
count = 0
for day in tempratures:
    count+=1
    print(f"day {count}: {average - day}")

print(f"Hottest day: {tempratures.argmax()}\n")
print(F"Days > 25: {(tempratures > 25).sum()}\n")

new_tempratures = np.where(tempratures> 30, tempratures+2 , tempratures)
print(f"new_tempratures: {new_tempratures}")

    