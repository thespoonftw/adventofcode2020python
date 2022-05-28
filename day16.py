from common import day

def part1(lines) -> int:
    return ticketSolver(lines).sumInvalids()

def part2(lines) -> int:
    return ticketSolver(lines).sumInvalids()

class ticketSolver:

    def __init__(self, lines):

        self.ruleDict = dict()
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
                self.ruleDict[split1[0]] = intList 

            elif linesPart == 1 and not line == "your ticket:":
                self.myTicket = list(map(int, line.split(",")))

            elif linesPart == 2 and not line == "nearby tickets:":
                ticket = list(map(int, line.split(",")))
                self.tickets.append(ticket)

    def sumInvalids(self):
        return sum([self.sumTicketInvalids(ticket) for ticket in self.tickets])

    def sumTicketInvalids(self, list):
        counter = 0
        for value in list:
            if (not self.IsValueValid(value)):
                counter += value
        return counter

    def IsValueValid(self, value):
        for rule in self.ruleDict.values():
            if (value >= rule[0] and value <= rule[1]) or (value >= rule[2] and value <= rule[3]):
                return True
        return False




day.run(part1, part2, 16)