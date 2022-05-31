from common import day
from enum import Enum
import math
import numpy

def part1(lines) -> int: 
    return Map(lines).solve()

def part2(lines) -> int:
    return 0

class Facing(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    

class Map:

    def __init__(self, lines):

        self.photos = list()
        
        i = 0
        while i < len(lines):
            id = int(lines[i][5:9])
            photoLines = lines[i+1:i+11]
            self.photos.append(Photo(id, photoLines))
            i += 12


    def solve(self) -> int:
        # find a tile to be our corner
        corner = self.findACorner()
        gridSize = int(math.sqrt(len(self.photos)))
        photoGrid = numpy.full((gridSize, gridSize), None)
        rotGrid = numpy.full((gridSize, gridSize), 0)
        photoGrid[0][0] = corner[0]
        rotGrid[0][0] = corner[1]

        a = self.findMatch(corner[0], corner[1], 0)
        b = self.findMatch(corner[0], corner[1], 1)
        c = self.findMatch(corner[0], corner[1], 2)
        d = self.findMatch(corner[0], corner[1], 3)



        for index in range(1, gridSize):
            prevPhoto = photoGrid[index - 1, 0]
            prevRot = rotGrid[index - 1, 0]
            match = self.findMatch(prevPhoto, prevRot, 1)
            x = 0

        #check = self.doEdgesMatch(self.photos[0], self.photos[1], 0, 0, 3)

        return 0 

    def findMatch(self, photo1, rot1, dir):
        for photo2 in self.photos:
            if (photo1 == photo2):
                continue
            for rot2 in range(4):
                if self.doEdgesMatch(photo1, photo2, rot1, rot2, dir):
                    return photo2, rot2


    def doEdgesMatch(self, photo1, photo2, rotation1, rotation2, direction):
        edge1 = photo1.getEdge(direction, rotation1)
        edge2 = list(reversed(photo2.getEdge((direction + 2) % 4, rotation2)))
        return edge1 == edge2      

    def findACorner(self) -> int:
        for photo1 in self.photos:
            neighbours = list()
            for photo2 in self.photos:
                if (photo1 == photo2):
                    continue
                for dir in range(4):
                    for rot in range(4):
                        if self.doEdgesMatch(photo1, photo2, 0, rot, dir):
                            neighbours.append(dir)
            if (len(neighbours) == 2):
                break

        neighbours.sort()
        if (neighbours == [0, 1]):
            return photo1, 0
        elif (neighbours == [1, 2]):
            return photo1, 1
        elif (neighbours == [2, 3]):
            return photo1, 2
        elif (neighbours == [0, 3]):
            return photo1, 3

        return -1



class Photo:

    def __init__(self, id, lines):
        self.id = id
        self.lines = lines

    def getEdge(self, edge, rotation):
        index = (edge - rotation) % 4
        if (index == 0): # north
            return [char for char in self.lines[0]]
        elif (index == 1): # east
            return [line[-1] for line in self.lines]
        elif (index == 2): # south
            return [char for char in reversed(self.lines[9])]
        elif (index == 3): # west
            return [line[0] for line in reversed(self.lines)]
        x = 0
        
        


day.run(part1, part2, 20)