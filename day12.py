from common import day
from enum import Enum

def part1(lines) -> int: 
    s = ship(lines)
    return s.solve()

def part2(lines) -> int:
    s = shipWithWaypoint(lines)
    return s.solve()

class Facing(Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3

class ship:

    def __init__(self, lines):
        self.lines = lines
        self.lat = 0
        self.lon = 0
        self.facing = Facing.EAST

    def solve(self) -> int:
        for line in self.lines:
            self.performAction(line)
        return abs(self.lat) + abs(self.lon)

    def performAction(self, line):

        char = line[0]
        value = int(line[1:])

        if char == "N":
            self.lat += value        
        elif char == "E":
            self.lon += value
        elif char == "S":
            self.lat -= value
        elif char == "W":
            self.lon -= value
        elif char == "R":
            self.facing = Facing((self.facing.value + value / 90) % 4)
        elif char == "L":
            self.facing = Facing((self.facing.value - value / 90) % 4)
        elif char == "F":
            if self.facing == Facing.EAST:
                self.lon += value
            elif self.facing == Facing.NORTH:
                self.lat += value
            elif self.facing == Facing.WEST:
                self.lon -= value
            elif self.facing == Facing.SOUTH:
                self.lat -= value


class shipWithWaypoint:

    def __init__(self, lines):
        self.lines = lines
        self.shipLat = 0
        self.shipLon = 0
        self.waypointLat = 1
        self.waypointLon = 10

    def solve(self) -> int:
        for line in self.lines:
            self.performAction(line)
        return abs(self.shipLat) + abs(self.shipLon)

    def performAction(self, line):

        char = line[0]
        value = int(line[1:])

        if char == "N":
            self.waypointLat += value        
        elif char == "E":
            self.waypointLon += value
        elif char == "S":
            self.waypointLat -= value
        elif char == "W":
            self.waypointLon -= value
        elif char == "R":
            self.rotate(value)
        elif char == "L":
            self.rotate(360 - value)
        elif char == "F":
            self.shipLat += self.waypointLat * value
            self.shipLon += self.waypointLon * value


    def rotate(self, amount):
        if (amount == 90):
            lat = self.waypointLat
            lon = self.waypointLon
            self.waypointLat = -lon
            self.waypointLon = lat

        elif (amount == 180):
            self.waypointLat = -self.waypointLat
            self.waypointLon = -self.waypointLon

        elif (amount == 270):
            lat = self.waypointLat
            lon = self.waypointLon
            self.waypointLat = lon
            self.waypointLon = -lat




day.run(part1, part2, 12)