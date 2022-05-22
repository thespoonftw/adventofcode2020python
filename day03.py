from common import day

def part1(lines) -> int: 
    grid = trees(lines)
    return grid.countTrees(3, 1)

def part2(lines) -> int:
    grid = trees(lines)
    n1 = grid.countTrees(1, 1)
    n2 = grid.countTrees(3, 1)
    n3 = grid.countTrees(5, 1)
    n4 = grid.countTrees(7, 1)
    n5 = grid.countTrees(1, 2)
    return n1 * n2 * n3 * n4 * n5

class trees: 

    def  __init__(self, lines):
        self.width = len(lines[0])
        self.height = len(lines)
        self.array = [[False for i in range(self.width)] for i in range(self.height)]

        for x in range(self.width): 
            for y in range(self.height):
                isTree = (lines[y][x] == '#')
                self.array[y][x] = isTree

    def countTrees(self, xSpeed, ySpeed) -> int: 
        
        treeCounter = 0
        yCurrent = 0
        xCurrent = 0

        while yCurrent < self.height:

            if self.array[yCurrent][xCurrent]:
                treeCounter += 1

            yCurrent += ySpeed
            xCurrent += xSpeed

            if xCurrent >= self.width:
                xCurrent -= self.width

        return treeCounter

day.run(part1, part2, 3)