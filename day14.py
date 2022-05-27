from common import day

def part1(lines) -> int:

    memory = [0 for i in range(99999)]

    currentMask = ""

    for line in lines:
        split = line.split(" = ")
        if split[0] == "mask":
            currentMask = split[1]
        else:
            location = int(split[0].split("[")[1][:-1])
            value = int(split[1])
            binary = format(value, '036b')
            binarySum = 0

            for i, char in enumerate(currentMask):
                power = 35 - i
                digit = int(char) if char != 'X' else int(binary[i])
                binarySum += digit * pow(2, power)

            memory[location] = binarySum

    return sum(memory)

def part2(lines) -> int:
    return 0
            


day.run(part1, part2, 14)