from common import day
import re

def part1(lines) -> int: 
    p1 = entries(lines)
    return p1.validEntries1()

def part2(lines) -> int:
    p2 = entries(lines)
    return p2.validEntries2()


class entries:

    def __init__(self, lines):

        self.entryList = list()
        i = 0
        length = len(lines)

        while (i < length):
            newEntry = entry() 

            while (i < length and lines[i] != ""):
                newEntry.addLine(lines[i])
                i += 1

            self.entryList.append(newEntry)
            i += 1

    def validEntries1(self) -> int:
        valids = [e for e in self.entryList if e.isValid1()]
        return len(valids)
    
    def validEntries2(self) -> int:
        valids = [e for e in self.entryList if e.isValid2()]
        return len(valids)



class entry: 

    def addLine(self, line):
        split = line.split(' ')
        for item in split:
            split2 = item.split(':')
            name = split2[0]
            desc = split2[1]
            if (name == "byr"):
                self.byr = desc
            elif (name == "iyr"):
                self.iyr = desc
            elif (name == "eyr"):
                self.eyr = desc
            elif (name == "hgt"):
                self.hgt = desc
            elif (name == "hcl"):
                self.hcl = desc 
            elif (name == "ecl"):
                self.ecl = desc
            elif (name == "pid"):
                self.pid = desc
            elif (name == "cid"):
                self.cid = desc

    def isValid1(self) -> bool:
        a = hasattr(self, "byr")
        b = hasattr(self, "iyr")
        c = hasattr(self, "eyr")
        d = hasattr(self, "hgt")
        e = hasattr(self, "hcl")
        f = hasattr(self, "ecl")
        g = hasattr(self, "pid")
        return a and b and c and d and e and f and g

    def isValid2(self) -> bool:

        if not self.isValid1():
            return False

        if len(self.hgt) < 4:
            return False

        b = self.byr.isdigit() and int(self.byr) >= 1920 and int(self.byr) <= 2002
        c = self.iyr.isdigit() and int(self.iyr) >= 2010 and int(self.iyr) <= 2020
        d = self.eyr.isdigit() and int(self.eyr) >= 2020 and int(self.eyr) <= 2030

        hgtPrefix = int(self.hgt[0:-2])
        hgtSuffix = self.hgt[-2:]
        cm = hgtSuffix == "cm" and hgtPrefix >= 150 and hgtPrefix <= 193
        inches = hgtSuffix == "in" and hgtPrefix >= 59 and hgtPrefix <= 76
        e = cm or inches 

        f = len(self.hcl) == 7 and self.hcl[0] == "#" and re.search("[a-f 0-9]", self.hcl[-6])

        g = self.ecl == "amb" or self.ecl == "blu" or self.ecl == "brn" or self.ecl == "gry" or self.ecl == "grn" or self.ecl == "hzl" or self.ecl == "oth"

        h = len(self.pid) == 9 and self.pid.isdigit() and int(self.pid) > 0

        return b and c and d and e and f and g and h


day.run(part1, part2, 4)