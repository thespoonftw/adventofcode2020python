from tkinter import E
from common import day
import numpy

def part1(lines) -> int: 
    r = reactor(lines, 20, False)
    r.cycle()
    r.cycle()
    r.cycle()
    r.cycle()
    r.cycle()
    r.cycle()
    #r.printPlane(5)
    return r.countOn()

def part2(lines) -> int:
    r = reactor(lines, 20, True)
    r.cycle()
    r.cycle()
    r.cycle()
    r.cycle()
    r.cycle()
    r.cycle()
    #r.printPlane(5)
    return r.countOn()

class reactor:

    def __init__(self, lines, size, is4D):

        self.is4D = is4D
        self.size = size

        wSize = size if is4D else 1 

        self.grid = numpy.full((self.size, self.size, self.size, wSize), False)

        offset = (size - len(lines)) // 2
        zOffset = size // 2
        wOffset = size // 2 if is4D else 0

        a = 0
        for line in lines:
            b = 0
            for char in line:
                if char == "#":
                    self.grid[b + offset][a + offset][zOffset][wOffset] = True
                b += 1
            a += 1


    def countOn(self):

        counter = 0
        wRange = range(self.size) if self.is4D else range(1)

        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    for w in wRange:
                        if self.grid[x][y][z][w] == True:
                            counter += 1
        
        return counter


    def cycle(self):

        wSize = self.size if self.is4D else 1
        wRange = range(1, self.size - 1) if self.is4D else range(1)
        newGrid = numpy.full((self.size, self.size, self.size, wSize), False)

        for x in range(1, self.size - 1):
            for y in range(1, self.size - 1):
                for z in range(1, self.size - 1):
                    for w in wRange:
                        count = self.countNeighbours(x, y, z, w)
                        if self.grid[x][y][z][w]:
                            if count == 2 or count == 3:
                                newGrid[x][y][z][w] = True
                            else:
                                newGrid[x][y][z][w] = False
                        else:
                            if count == 3:
                                newGrid[x][y][z][w] = True

        self.grid = newGrid


    def countNeighbours(self, x, y, z, w) -> int:

        counter = 0
        wRange = range (-1, 2) if self.is4D else range(1)

        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    for l in wRange:
                        if (i == 0 and j == 0 and k == 0 and l == 0): 
                            continue
                        if (self.grid[x + i][y + j][z + k][w + l]):
                            counter += 1

        return counter

    def printPlane(self, z, w):
        
        for y in range(0, self.size):

            line = ""
            for x in range(0, self.size):
                if (self.grid[x][y][z][w]):
                    line += "#"
                else:
                    line += "."

            print(line)


day.run(part1, part2, 17)