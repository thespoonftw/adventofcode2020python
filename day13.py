from common import day
import numpy

def part1(lines) -> int: 
    startTime = int(lines[0])
    busesSplit = lines[1].split(",")
    bestBus = 0
    bestTime = startTime * 2 # start with some arbitrarily high time

    for busStr in busesSplit:
        if (busStr != "x"):
            busInt = int(busStr)
            catchTime = (int(startTime / busInt) * busInt) + busInt
            if (catchTime < bestTime):
                bestBus = busInt
                bestTime = catchTime
    
    return bestBus * (bestTime - startTime)

def part2(lines) -> int:
    busesSplit = lines[1].split(",")
    t = 0
    lcm = int(busesSplit[0])
    i = 1
    while (i < len(busesSplit)):
        if (busesSplit[i] != "x"):
            busInt = int(busesSplit[i])

            # keep adding lcm to t until next term is mod 0
            while (t + i) % busInt != 0:
                t += lcm

            lcm = getLcm(lcm, busInt)
        i += 1

    return t
            
            
def getLcm(a, b) -> int:
    return a * b  
    # this was a placehold but seems to actually work, lol


day.run(part1, part2, 13)