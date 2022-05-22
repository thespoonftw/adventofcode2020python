from common import day

def part1(lines) -> int: 

    counter = 0
    groupSet = set()
    length = len(lines)
    i = 0

    while i < length:

        while (i < length and lines[i] != ""):
            for char in lines[i]:
                groupSet.add(char)
            i += 1

        counter += len(groupSet)
        groupSet = set()
        i += 1
        

    return counter

def part2(lines) -> int:
    
    counter = 0
    length = len(lines)
    i = 0

    while i < length:

        mySet = set(lines[i])
        i += 1

        while (i < length and lines[i] != ""):

            mySet = mySet & set(lines[i])
            i += 1
            

        counter += len(mySet)
        i += 1

    return counter


day.run(part1, part2, 6)