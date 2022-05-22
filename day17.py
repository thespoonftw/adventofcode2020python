from msilib.schema import IsolatedComponent
from common import day

def part1(lines) -> int: 
    r = reactor(lines, 4)
    
    r.cycle()
    
    
    
    return r.countOn()

def part2(lines) -> int:
    return 0

class reactor:

    def __init__(self, lines, size):

        self.n = size * 2
        self.grid = [[[False for k in range(self.n)] for j in range(self.n)] for i in range(self.n)]
        offset = 1

        a = 0
        for line in lines:
            b = 0
            for char in line:
                if char == "#":
                    self.grid[b + offset][a + offset][size] = True
                b += 1
            a += 1


    def countOn(self):

        counter = 0

        for x in range(self.n):
            for y in range(self.n):
                for z in range(self.n):
                    if self.grid[x][y][z] == True:
                        counter += 1
        
        return counter


    def cycle(self):

        newGrid = [[[False for k in range(self.n)] for j in range(self.n)] for i in range(self.n)]

        for x in range(1, self.n - 1):
            for y in range(1, self.n - 1):
                for z in range(1, self.n - 1):
                    count = self.countNeighbours(x, y, z)
                    if self.grid[x][y][z]:
                        if count == 2 or count == 3:
                            newGrid[x][y][z] = True
                        else:
                            newGrid[x][y][z] = False
                    else:
                        if count == 3:
                            newGrid[x][y][z] = True

        self.grid = newGrid

        x = 1


    def countNeighbours(self, x, y, z) -> int:

        counter = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if (i == 0 and j == 0 and k == 0): 
                        continue
                    if (self.grid[x + i][y + j][z + k]):
                        counter += 1
        
        if (counter > 1):
            b = 0

        return counter

    def printPlane(self, z):
        
        for y in range(0, self.n):

            line = ""
            for x in range(0, self.n):
                if (self.grid[x][y][z]):
                    line += "#"
                else:
                    line += "."

            print(line)


day.run(part1, part2, 17)