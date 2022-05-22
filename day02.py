from common import day

def part1(lines) -> int: 
    valids = [line for line in lines if password(line).isValid1()]
    return len(valids)

def part2(lines) -> int:
    valids = [line for line in lines if password(line).isValid2()]
    return len(valids)



class password: 

    def  __init__(self, line):
        split1 = line.split(': ')
        self.password = split1[1]
        split2 = split1[0].split(' ')
        self.char = split2[1]
        split3 = split2[0].split('-')
        self.a = int(split3[0])
        self.b = int(split3[1])

    def isValid1(self) -> bool: 
        count = self.password.count(self.char)
        return (count >= self.a) and (count <= self.b)

    def isValid2(self) -> bool:
        checkOne = self.password[self.a - 1] == self.char
        checkTwo = self.password[self.b - 1] == self.char
        return checkOne ^ checkTwo

day.run(part1, part2, 2)