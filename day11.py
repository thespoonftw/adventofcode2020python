from common import day
import numpy

def part1(lines) -> int: 
    s = seating(lines, True)
    return s.countStability()

def part2(lines) -> int:
    s = seating(lines, False)
    return s.countStability()

class seating:

    TIME_OUT = 10000
    OCCUPIED_CHAR = "#"
    EMPTY_CHAR = "L"
    FLOOR_CHAR = "."


    def __init__(self, lines, isPart2):
        self.height = len(lines)
        self.width = len(lines[0])
        self.xRange = range(self.width)
        self.yRange = range(self.height)
        self.grid = numpy.full((self.height, self.width), self.FLOOR_CHAR)
        self.isPart2 = isPart2
        self.threshold = 5 if isPart2 else 4

        for x in self.xRange:
            for y in self.yRange:
                self.grid[y][x] = lines[y][x]

    def countStability(self) -> int:
        prevCount = -1
        for i in range(self.TIME_OUT):
            self.performCycle()
            newCount = self.countChar(self.OCCUPIED_CHAR)
            #self.print()
            if (prevCount == newCount):
                return newCount
            else:
                prevCount = newCount
        print("Timed out")
        return -1

    def countChar(self, char) -> int:
        counter = 0
        for x in self.xRange:
            for y in self.yRange:
                if char == self.grid[y][x]:
                    counter += 1
        return counter

    def print(self):
        for y in self.yRange:
            printStr = ""
            for x in self.xRange:
                printStr += self.grid[y][x]
            print(printStr)
        print(" ")


    def performCycle(self):
        newGrid = numpy.full((self.height, self.width), self.FLOOR_CHAR)

        for x in self.xRange:
            for y in self.yRange:
                char = self.grid[y][x]
                if char == self.FLOOR_CHAR:
                    continue

                neighbours = self.countNeighbours(x, y)
                if char == self.EMPTY_CHAR and neighbours == 0:
                    newGrid[y][x] = self.OCCUPIED_CHAR
                elif char == self.OCCUPIED_CHAR and neighbours >= self.threshold:
                    newGrid[y][x] = self.EMPTY_CHAR
                else:
                    newGrid[y][x] = self.grid[y][x]

        self.grid = newGrid                

    def countNeighbours(self, x, y) -> int:
        counter = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                elif self.getSeenSeat(x, y, i, j) == self.OCCUPIED_CHAR:
                    counter += 1

        return counter

    def getSeenSeat(self, x, y, xDir, yDir) -> str:
        i = 1
        while (True):
            xCheck = x + (xDir * i)
            yCheck = y + (yDir * i)
            if (xCheck < 0 or yCheck < 0 or xCheck == self.width or yCheck == self.height):
                return self.EMPTY_CHAR
            seat = self.grid[yCheck, xCheck]

            if (not self.isPart2):
                return seat
            elif (seat != self.FLOOR_CHAR):
                return seat
            else:
                i += 1



day.run(part1, part2, 11)