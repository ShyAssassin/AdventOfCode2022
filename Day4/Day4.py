with open("Input.txt", 'r') as file:
    counter = 0
    overlapCounter = 0
    for line in file:
        e1, e2 = line.split(",")
        e1Start, e1End = int(e1.split("-")[0]), int(e1.split("-")[1])
        e2Start, e2End = int(e2.split("-")[0]), int(e2.split("-")[1])
        if (e1Start <= e2Start and e1End >= e2End) or (e2Start <= e1Start and e2End >= e1End):
            counter += 1
        if (set(range(e1Start, e1End + 1)) & (set(range(e2Start, e2End + 1)))):
            overlapCounter += 1

print(f"Part 1: {counter}")
print(f"Part 2: {overlapCounter}")