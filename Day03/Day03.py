def CalculateScore(c: str) -> int:
    if c.isupper():
        return int(ord(c) - ord("A") + 27)
    else:
        return int(ord(c) - ord("a") + 1)


Score1 = 0
with open("Input.txt", "r") as file:
    for line in file:
        line = line.strip()
        FirstHalf, SecondHalf = line[: len(line) // 2], line[len(line) // 2 :]
        for letter in FirstHalf:
            if letter in SecondHalf:
                Score1 += CalculateScore(letter)
                break


Score2 = 0
with open("Input.txt", "r") as file:
    lines = file.readlines()
    i = 0
    while i < len(lines):
        for letter in lines[i]:
            if letter in lines[i + 1] and letter in lines[i + 2]:
                Score2 += CalculateScore(letter)
                break
        i += 3

print(f"Part 1: {Score1}")
print(f"Part 2: {Score2}")
