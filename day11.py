from common import day
import numpy

def part1(lines) -> int: 
    s = seating(lines)
    return s.countStability()

def part2(lines) -> int:
    
    return 0

class seating:

    TIME_OUT = 10000
    OCCUPIED_CHAR = "#"
    EMPTY_CHAR = "L"
    FLOOR_CHAR = "."


    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.xRange = range(self.width)
        self.yRange = range(self.height)
        self.grid = numpy.full((self.height, self.width), self.FLOOR_CHAR)

        for x in self.xRange:
            for y in self.yRange:
                self.grid[x][y] = lines[x][y]

        self.print()

    def countStability(self) -> int:
        prevCount = -1
        for i in range(self.TIME_OUT):
            self.performCycle()
            self.print()
            newCount = self.countChar(self.OCCUPIED_CHAR)            
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
                if char == self.grid[x][y]:
                    counter += 1
        return counter

    def print(self):
        for y in self.yRange:
            print(self.grid[0:self.width][y])
        print(" ")


    def performCycle(self):
        newGrid = numpy.full((self.width, self.height), self.FLOOR_CHAR)

        for x in self.xRange:
            for y in self.yRange:
                char = self.grid[x][y]
                if char == self.FLOOR_CHAR:
                    continue

                neighbours = self.countNeighbours(x, y)
                if char == self.EMPTY_CHAR and neighbours == 0:
                    newGrid[x][y] = self.OCCUPIED_CHAR
                elif char == self.OCCUPIED_CHAR and neighbours >= 4:
                    newGrid[x][y] = self.EMPTY_CHAR
                else:
                    newGrid[x][y] = self.grid[x][y]

        self.grid = newGrid                

    def countNeighbours(self, x, y) -> int:
        xStart = x - 1 if x > 0 else 0
        xEnd = x + 1 if x < self.width - 1 else self.width - 1
        yStart = y - 1 if y > 0 else 0
        yEnd = y + 1 if y < self.width - 1 else self.width - 1
        counter = 0

        for i in range(xStart, xEnd):
            for j in range(yStart, yEnd):
                if i == x and j == y:
                    continue
                elif self.grid[i][j] == self.OCCUPIED_CHAR:
                    counter += 1

        return counter

day.run(part1, part2, 11)