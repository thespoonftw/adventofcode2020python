from common import day

def part1(lines) -> int: 
    ints = list(map(int, lines))
    length = len(lines)

    # set preamble length for test / not test case
    preambleLength = 25 if length != 20 else 5

    # check each value from end of preamble to end of sequence
    i = preambleLength    
    while (i < length):

        start = i - preambleLength
        j = start
        isPairFound = False

        # for each pair of values from start to i
        while (j < i and not isPairFound):
            k = start
            while (k < i and not isPairFound):

                if (j != k and ints[j] + ints[k] == ints[i]):
                    isPairFound = True

                k += 1
            j += 1

        if (not isPairFound):
            return ints[i]

        i += 1

    # no value found
    return 0

def part2(lines) -> int:
    ints = list(map(int, lines))
    sumValue = part1(lines)
    length = len(lines)

    # start index of our sum
    i = 0
    while (i < length):
        
        # end index of our sum
        j = i + 1

        while (j < length):
            thisList = ints[i:(j + 1)]
            thisSum = sum(thisList)

            if (thisSum == sumValue):
                return min(thisList) + max(thisList)
            elif (thisSum > sumValue):
                break
            else:
                j += 1

        i += 1

    # no value found
    return 0

class executer:

    def __init__(self, lines):
        x = 0

    





day.run(part1, part2, 9)