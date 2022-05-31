from pandas import array
from common import day

def part1(lines) -> int: 
    return MessageVerifier(lines, False).solve()

def part2(lines) -> int:
    return MessageVerifier(lines, True).solve()

class Rule:

    def setRuleStr(self, ruleStr):
        self.ruleStr = ruleStr

    def getRuleStr(self) -> str:
        return self.ruleStr

    def setLetter(self, letter):
        self.letter = letter
        self.ruleType = 0

    def setRuleset(self, rules):
        self.rules = rules
        self.ruleType = 1

    def setOrRules(self, leftRule, rightRule):
        self.leftRule = leftRule
        self.rightRule = rightRule
        self.ruleType = 2

    def setRecursive8(self, rule42):
        self.ruleType = 8
        self.rule42 = rule42

    def setRecursive11(self, rule42, rule31):
        self.ruleType = 11
        self.rule42 = rule42
        self.rule31 = rule31

    def getPossibilities(self) -> set:
        if (not hasattr(self, "possibilities")):
            pos = set()
            self.possibilities = pos

            if (self.ruleType == 0):
                pos.add(self.letter)

            elif (self.ruleType == 1):
                listOfSets = [rule.getPossibilities() for rule in self.rules]
                results = self.combinePossibilities(listOfSets)
                for result in results:
                    pos.add(result)

            elif (self.ruleType == 2):
                for result1 in self.leftRule.getPossibilities():
                    pos.add(result1)
                for result2 in self.rightRule.getPossibilities():
                    pos.add(result2)

            elif (self.ruleType == 8):
                set42 = self.rule42.getPossibilities()
                listOfSets = [ set42 ]
                results = self.combinePossibilities(listOfSets)
                for result in results:
                    pos.add(result)

            elif (self.ruleType == 11):
                for result1 in self.rule42.getPossibilities():
                    for result2 in self.rule31.getPossibilities():
                        pos.add(result1 + result2)

        return self.possibilities

    def combinePossibilities(self, listOfSets) -> set:
        # only 1 set, return it
        if (len(listOfSets) == 1):
            return tuple(listOfSets)[0] # retrieve only item in set

        setsSoFar = set().union(listOfSets[0])
        i = 1

        while i < len(listOfSets):
            nextSet = set()
            for prefix in setsSoFar:
                for suffix in listOfSets[i]:
                    nextSet.add(prefix + suffix)
            setsSoFar = nextSet
            i += 1

        return setsSoFar
        


class MessageVerifier:

    def __init__(self, lines, isPartTwo):

        self.rules = dict()
        self.messages = list()
        self.isPartTwo = isPartTwo
        self.maxLength = len(max(lines, key=len))

        isReadingMessages = False
        for line in lines:

            if line == "":
                isReadingMessages = True

            elif isReadingMessages:
                binary = line.replace("a", "0").replace("b", "1")
                self.messages.append(int(binary, 2))

            else:    
                split = line.split(": ")
                value = Rule()
                ruleInt = int(split[0])
                value.setRuleStr(split[1])
                self.rules[ruleInt] = value

        for key, value in self.rules.items():

            ruleStr = value.getRuleStr()

            if (isPartTwo and key == 8):
                value.setRecursive8(self.rules[42])       

            elif (isPartTwo and key == 11):
                value.setRecursive11(self.rules[42], self.rules[31])  

            elif (ruleStr == '"a"'):
                value.setLetter("0")

            elif (ruleStr == '"b"'):
                value.setLetter("1")
                
            elif ('|' in ruleStr):
                split2 = ruleStr.split(" | ")
                leftRule = Rule()
                leftRule.setRuleset(self.getRulesForRuleStr(split2[0]))
                rightRule = Rule()
                rightRule.setRuleset(self.getRulesForRuleStr(split2[1]))
                value.setOrRules(leftRule, rightRule)

            else:
                value.setRuleset(self.getRulesForRuleStr(ruleStr))


    def getRulesForRuleStr(self, ruleStr) -> list:
        ints = list(map(int, ruleStr.split(" ")))
        return [self.rules[i] for i in ints]


    def solve(self) -> int:
        possibilities = self.rules[0].getPossibilities()
        ints = [int(item, 2) for item in possibilities]
        ints.sort()
        counter = 0
        for message in self.messages:
           if self.binarySearch(ints, message, 0, len(ints)):
               counter += 1
        return counter

    def binarySearch(self, array, element, start, end) -> bool:
        if start > end:
            return False
        mid = (start + end) // 2
        if element == array[mid]:
            return True
        if element < array[mid]:
            return self.binarySearch(array, element, start, mid-1)
        else:
            return self.binarySearch(array, element, mid+1, end)



        

day.run(part2, part1, 19)