from common import day

def part1(lines) -> int:
    return ticketSolver(lines).solvePartOne()

def part2(lines) -> int:
    return ticketSolver(lines).solvePartTwo()

class ticketSolver:

    def __init__(self, lines):

        self.rules = list()
        self.tickets = list()
        linesPart = 0

        for line in lines:

            if line == "":
                linesPart += 1

            elif linesPart == 0:
                split1 = line.split(": ")
                split2 = split1[1].split(" or ")
                split3 = split2[0].split("-")
                split4 = split2[1].split("-")
                intList = list()
                intList.append(int(split3[0]))
                intList.append(int(split3[1]))
                intList.append(int(split4[0]))
                intList.append(int(split4[1]))
                self.rules.append(intList) 

            elif linesPart == 1 and not line == "your ticket:":
                self.myTicket = list(map(int, line.split(",")))

            elif linesPart == 2 and not line == "nearby tickets:":
                ticket = list(map(int, line.split(",")))
                self.tickets.append(ticket)

        self.length = len(self.rules)
        self.validTickets = [ticket for ticket in self.tickets if self.isTicketValid(ticket)]

    def isTicketValid(self, ticket) -> bool:
        for value in ticket:
            if not self.isValueValidForAnyRule(value):
                return False
        return True

    def isValueValidForAnyRule(self, value) -> bool:
        for rule in self.rules:
            if self.isValueValidForRule(value, rule):
                return True
        return False

    def isValueValidForRule(self, value, rule) -> bool:
        return value >= rule[0] and value <= rule[1] or (value >= rule[2] and value <= rule[3])

    def isColumnValidForRule(self, columnIndex, rule) -> bool:
        for ticket in self.validTickets:
            value = ticket[columnIndex]
            if not self.isValueValidForRule(value, rule):
                return False
        return True


    def solvePartOne(self) -> int:
        counter = 0
        for ticket in self.tickets:
            for value in ticket:
                if (not self.isValueValidForAnyRule(value)):
                    counter += value
        return counter

    def solvePartTwo(self) -> int:
        # return -1 on test
        if (len(self.rules) == 3):
            return -1 
        
        # find all possible columns for each rule
        columnSets = list()
        for rule in self.rules:
            columnSet = set()
            columnIndex = 0
            while columnIndex < self.length:
                if self.isColumnValidForRule(columnIndex, rule):
                    columnSet.add(columnIndex)
                columnIndex += 1
            columnSets.append(columnSet)

        columnsForRule = dict()
        checkIteration = 0
        # repeat algorithm to make sure all solutions are found (not the most efficient)
        while checkIteration < self.length:

            # check each rule to see if there is only 1 possible solution
            ruleIndex = 0
            while ruleIndex < self.length:
                if len(columnSets[ruleIndex]) == 1:
                    columnIndex = min(columnSets[ruleIndex]) # min here selects the only item from the set
                    columnsForRule[ruleIndex] = columnIndex
                    for columnSet in columnSets:
                        columnSet.discard(columnIndex) # discard removes item if exists
                    break
                ruleIndex += 1

            checkIteration += 1

        # multiply the results together
        returner = 1
        for index in range(0, 6):
            returner *= self.myTicket[columnsForRule[index]]
        return returner

day.run(part1, part2, 16)