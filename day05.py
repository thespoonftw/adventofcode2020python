from common import day

def part1(lines) -> int: 
    seatValues = [seat(l).getValue() for l in lines]
    return max(seatValues)

def part2(lines) -> int:
    seatValues = [seat(l).getValue() for l in lines]
    seatValues.sort()
    i = 0
    while (i < len(seatValues)):
        if (seatValues[i] + 1 != seatValues[i + 1]):
            return seatValues[i] + 1
        i += 1


class seat:

    def __init__(self, line):
        rowString = line[0:7].replace("F", "0").replace("B", "1")
        columnString = line[7:10].replace("L", "0").replace("R", "1")
        self.row = int(rowString, 2)
        self.column = int(columnString, 2)

    def getRow(self) -> int:
        return self.row

    def getColumn(self) -> int:
        return self.column

    def getValue(self) -> int:
        return self.row * 8 + self.column


day.run(part1, part2, 5)