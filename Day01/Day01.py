ElfCalories = []

Calories = 0
with open("Input.txt", "r") as file:
    for line in file:
        if line != "\n":
            Calories += int(line)
        else:
            ElfCalories.append(Calories)
            Calories = 0

ElfCalories = sorted(ElfCalories)
print(f"Part 1: {ElfCalories[-1]}")
print(f"Part 2: {ElfCalories[-1]+ElfCalories[-2]+ElfCalories[-3]}")
