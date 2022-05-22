from msilib.schema import IsolatedComponent
from common import day

def part1(lines) -> int: 
    e = executer(lines)
    e.runCode()
    return e.getAccum()

def part2(lines) -> int:
    i = 0
    while (i < len(lines)):
        e = executer(lines)
        e.setInverter(i)
        e.runCode()
        if (e.getIsComplete()):
            return e.getAccum()
        i += 1
    return 0

class executer:

    def __init__(self, lines):
        self.lines = lines
        self.inverter = -1
        self.length = len(lines)
        self.accum = 0
        self.isComplete = False

    def setInverter(self, index):
        self.inverter = index

    def getAccum(self) -> int:
        return self.accum

    def getIsComplete(self):
        return self.isComplete

    def runCode(self):
        i = 0
        visited = set()
        visited.add(0)

        while (True):
            line = self.lines[i]
            split = line.split(" ")
            instruction = split[0]
            amount = int(split[1])

            if ((instruction == "nop" and self.inverter != i) or (instruction == "jmp" and self.inverter == i)):
                i += 1

            elif (instruction == "acc"):
                self.accum += amount
                i += 1

            elif ((instruction == "jmp" and self.inverter != i) or (instruction == "nop" and self.inverter == i)):
                i += amount

            if (i >= self.length):
                self.isComplete = True
                break

            if (i in visited):
                break

            visited.add(i)     





day.run(part1, part2, 8)