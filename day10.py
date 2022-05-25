from common import day

def part1(lines) -> int: 
    ints = getInts(lines)

    ones = 0
    threes = 0
    length = len(ints)
    i = 0

    while (i < length - 1):
        if (ints[i] + 1 == ints[i + 1]):
            ones += 1
        if (ints[i] + 3 == ints[i + 1]):
            threes += 1

        i += 1

    return ones * threes

def part2(lines) -> int:
    ints = getInts(lines)

    length = len(ints)
    pathsList = [None] * length

    # work forwards to create list of possible paths
    i = 0
    while (i < length - 1):
        paths = list()
        if (ints[i + 1] <= ints[i] + 3):
            paths.append(i + 1)
        if (i < length - 2 and ints[i + 2] <= ints[i] + 3):
            paths.append(i + 2)
        if (i < length - 3 and ints[i + 3] <= ints[i] + 3):
            paths.append(i + 3)

        pathsList[i] = paths
        i += 1

    # work backwards to work out value of each path
    i = length - 2
    pathsValue = [None] * length
    pathsValue[length - 1] = 1

    while (i >= 0):
        sum = 0
        for path in pathsList[i]:
            sum += pathsValue[path]
        pathsValue[i] = sum
        i -= 1

    return pathsValue[0]

def getInts(lines) -> list:
    ints = list(map(int, lines))
    ints.append(0)    
    ints.sort()
    ints.append(ints[len(ints) - 1] + 3)
    return ints

def countCombos(ints) -> int:
    return len(ints)

class executer:

    def __init__(self, lines):
        x = 0

    





day.run(part1, part2, 10)