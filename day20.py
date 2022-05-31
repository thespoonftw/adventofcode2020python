from tkinter import E
from common import day
from enum import Enum
import math
import numpy

def part1(lines) -> int: 
    return Map(lines).solvePart1()

def part2(lines) -> int:
    return 0

class Facing(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Orienation(Enum):
    n0r0 = 0 # normal rotation 0
    n0r1 = 1
    n0r2 = 2
    n0r3 = 3
    m0r0 = 4
    m0r1 = 5
    m0r2 = 6
    m0r3 = 7
    

class Map:

    def __init__(self, lines):

        self.photos = list()
        
        i = 0
        while i < len(lines):
            id = int(lines[i][5:9])
            photoLines = lines[i+1:i+11]
            self.photos.append(Photo(id, photoLines))
            i += 12


    def solvePart1(self) -> int:
        corners = self.findCorners()
        multiplier = 1
        for corner in corners:
            multiplier *= corner.id
        return multiplier

    def findMatch(self, photo1, ori1, dir):
        for photo2 in self.photos:
            if (photo1 == photo2):
                continue
            for ori2 in range(8):
                if self.doEdgesMatch(photo1, photo2, ori1, ori2, dir):
                    return photo2, ori2


    def doEdgesMatch(self, photo1, photo2, orientation1, orientation2, direction):
        edge1 = photo1.getEdge(direction, orientation1)
        oppositeDirection = (direction + 2) % 4
        edge2 = list(reversed(photo2.getEdge(oppositeDirection, orientation2)))
        return edge1 == edge2      

    def findCorners(self) -> int:
        returner = list()
        for photo1 in self.photos:
            neighbours = 0
            for photo2 in self.photos:
                if (photo1 == photo2):
                    continue
                for edge1 in photo1.allEdges:
                    for edge2 in photo2.allEdges:
                        if edge1 == edge2:
                            neighbours += 1
            if (neighbours == 4):
                returner.append(photo1)

        return returner



class Photo:

    def __init__(self, id, lines):
        self.id = id
        self.lines = lines

        northEdge = ''.join([char for char in self.lines[0]])
        eastEdge = ''.join([line[-1] for line in self.lines])
        southEdge = ''.join([char for char in list(reversed(self.lines[9]))])
        westEdge = ''.join([line[0] for line in list(reversed(self.lines))])

        self.normalEdges = [ northEdge, eastEdge, southEdge, westEdge ]
        self.mirrorEdges = [ northEdge[::-1], westEdge[::-1], southEdge[::-1], eastEdge[::-1] ]
        self.allEdges = self.normalEdges + self.mirrorEdges

    def getEdge(self, index, orientation):
        if (orientation < 4):
            mod = (index - orientation) % 4
            return self.normalEdges[mod]
        else:
            mod = (index + orientation) % 4
            return self.mirrorEdges[mod]
        


day.run(part1, part2, 20)