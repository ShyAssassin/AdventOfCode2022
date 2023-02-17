with open("Input.txt") as file:
    data = file.read()


def solve(data, n=4):
    # some cursed shit right here
    groups = [(data[i : i + n]) for i in range(0, len(data) - n + 1)]
    for i, group in enumerate(groups):
        if len(set(group)) == len(group):
            return i + n


print(f"Part 1: {solve(data, n=4)}")
print(f"Part 2: {solve(data, n=14)}")
