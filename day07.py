from common import day

def part1(lines) -> int: 

    rules = bagrules(lines)
    return rules.countGoldBags()

def part2(lines) -> int:
    
    rules = bagrules(lines)
    return rules.countBagsInside("shiny gold")

class bagrules:

    def __init__(self, lines):

        self.allrules = dict()

        for line in lines:

            split1 = line.split(" bags contain ")
            name = split1[0]
            thisrule = dict()
            self.allrules[name] = thisrule

            if split1[1] != "no other bags.":

                split2 = split1[1][:-1].split(", ")
            
                for item in split2:
                    words = item.split(" ")
                    amount = int(words[0])
                    colour = words[1] + " " + words[2]
                    thisrule[colour] = amount

        x = 1


    def countGoldBags(self) -> int:

        counter = 0

        for ruleKey in self.allrules:
            if self.isGoldInBag(ruleKey):
                counter += 1

        return counter


    def isGoldInBag(self, bagName) -> bool:
        
        contents = self.allrules[bagName]

        if "shiny gold" in contents:
            return True

        for ruleKey in contents:
            if self.isGoldInBag(ruleKey):
                return True

        return False


    def countBagsInside(self, bagName) -> int:

        contents = self.allrules[bagName]
        counter = 0

        for bagName in contents:
            multiplier = contents[bagName]
            counter += multiplier + (multiplier * self.countBagsInside(bagName))

        return counter


day.run(part1, part2, 7)