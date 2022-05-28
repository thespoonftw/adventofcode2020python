from dataclasses import replace
from common import day

def part1(lines) -> int:
    return solve(lines, False)
    

def part2(lines) -> int:
    return solve(lines, True)

def solve(lines, isPartTwo) -> int:
    memory = dict()
    currentMask = ""

    for line in lines:
        split = line.split(" = ")
        if split[0] == "mask":
            currentMask = split[1]
        else:
            location = int(split[0].split("[")[1][:-1])
            value = int(split[1])
            if (isPartTwo):
                for newLocation in applyMaskToLocations(currentMask, location):
                    memory[newLocation] = value
            else:
                memory[location] = applyMaskToValue(currentMask, value)
            

    return sum(memory.values())

def applyMaskToValue(mask, value) -> int:
    binary = format(value, '036b')
    binarySum = 0
    for i, char in enumerate(mask):
        power = 35 - i
        digit = int(char) if char != 'X' else int(binary[i])
        binarySum += digit * pow(2, power)

    return binarySum

def applyMaskToLocations(mask, location) -> list:
    returner = list()
    binary = format(location, '036b')
    recursiveFindValues(mask, binary, returner, 0)
    return returner

def recursiveFindValues(mask, binary, returner, index):
    if (index == len(mask)):
        returner.append(int(binary, 2))
        return
    
    char = mask[index]
    if (char == "X"):
        newBinary1 = replaceChar(binary, index, "1")
        newBinary2 = replaceChar(binary, index, "0") 
        recursiveFindValues(mask, newBinary1, returner, index + 1)
        recursiveFindValues(mask, newBinary2, returner, index + 1)

    elif (char == "1"):
        newBinary = replaceChar(binary, index, "1")
        recursiveFindValues(mask, newBinary, returner, index + 1)

    elif (char == "0"):
        recursiveFindValues(mask, binary, returner, index + 1)

def replaceChar(string, index, char):
    return string[0:index] + char + string[index+1:]

day.run(part1, part2, 14)