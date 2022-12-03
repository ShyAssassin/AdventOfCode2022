# Rock = A, X
# Paper = B, y
# Scissors = C, Z

Combinations = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}
PerfectCombinations = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

Score = 0
PerfectScore = 0
with open("Input.txt", "r") as file:
    for line in file:
        line = line.strip()
        Score += Combinations[line]
        PerfectScore += PerfectCombinations[line]

print("Part 1:", Score)
print("Part 2:", PerfectScore)