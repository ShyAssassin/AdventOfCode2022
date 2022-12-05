import copy


def CreateCrateArray(stack, size, crates):
    index = 1
    for i in range(size):
        for row in reversed(stack):
            if (row[index] == ' '):
                break
            crates[i].append(row[index])
        index += 4


stackSize = 0
rawStack = []
instructions = []
with open('Input.txt', "r") as file:
    reading_stack = True
    for line in file:
        if reading_stack:
            if line == "\n":
                reading_stack = False
                # remove numbers denoting stack size
                rawStack.pop(-1)
            else:
                stackSize += 1
                rawStack.append(line)
        else:
            instructions.append(line.strip().split(' '))


base_stack = [[] for i in range(stackSize)]
CreateCrateArray(rawStack, stackSize, base_stack)


p1Stacks = copy.deepcopy(base_stack)
for move in instructions:
    moveAmount = int(move[1])
    fromIndex = int(move[3])
    destinationIndex = int(move[5])

    for _ in range(moveAmount):
        crate = p1Stacks[fromIndex-1].pop()
        p1Stacks[destinationIndex-1].append(crate)
print(f"Part 1: {''.join([stack[-1] for stack in p1Stacks])}")


p2Stacks = copy.deepcopy(base_stack)
for move in instructions:
    moveAmount = int(move[1])
    fromIndex = int(move[3])
    destinationIndex = int(move[5])
    crates = p2Stacks[fromIndex-1][-moveAmount:]  
    del p2Stacks[fromIndex-1][-moveAmount:]
    p2Stacks[destinationIndex-1].extend(crates)        
print(f"Part 2: {''.join([stack[-1] for stack in p2Stacks])}")