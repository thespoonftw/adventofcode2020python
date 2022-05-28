from common import day

def part1(lines) -> int:
    return solver(lines).solve(2020)

def part2(lines) -> int:
    return solver(lines).solve(30000000)

class solver:

    def __init__(self, lines):

        intList = list(map(int, lines[0].split(",")))
        self.intDict = dict()
        self.startIndex = len(intList) - 1
        self.lastValue = intList[-1]
        self.debugList = list(map(int, lines[0].split(",")))
        for i in range(self.startIndex):
            self.intDict[intList[i]] = i
        

    def solve(self, endIndex):
        for i in range(self.startIndex, endIndex - 1):
            val = self.findNextValue(i)
            self.debugList.append(val)
            self.intDict[self.lastValue] = i
            self.lastValue = val
            

        return self.lastValue

    def findNextValue(self, index) -> int:

        if (not self.lastValue in self.intDict):
            return 0

        else:
            lastSeen = self.intDict[self.lastValue]
            return index - lastSeen


day.run(part1, part2, 15)