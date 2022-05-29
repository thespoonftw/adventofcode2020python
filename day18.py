from common import day

def part1(lines) -> int: 
    return solve(lines, False)

def part2(lines) -> int:
    return solve(lines, True)

def solve(lines, isPartTwo) -> int:
    returner = 0
    for line in lines:
        convertedLine = line.replace("(", "( ").replace(")", " )").split(" ")
        returner += Expression(convertedLine, isPartTwo).evaluate()
    return returner


class Expression:

    def __init__(self, entries, isPartTwo):
        self.items = list()
        self.operators = list()
        self.isPartTwo = isPartTwo

        tally = 0

        for index, entry in enumerate(entries):

            if entry == "(":
                if tally == 0:
                    startIndex = index
                tally += 1
                

            elif entry == ")":
                tally -= 1
                if tally == 0:
                    expressionItems = entries[startIndex+1:index]
                    self.items.append(Expression(expressionItems, isPartTwo))

            elif entry == "+" or entry == "*":
                if tally == 0:
                    self.operators.append(entry)

            else:
                if tally == 0:
                    self.items.append(int(entry))


    def evaluate(self) -> int:

        if (not self.isPartTwo):
            leftTerm = self.evaluateTerm(self.items[0])

            for index in range(len(self.operators)):
                nextTerm = self.evaluateTerm(self.items[index + 1])
                operator = self.operators[index]
                if (operator == "+"):
                    leftTerm += nextTerm
                elif (operator == "*"):
                    leftTerm *= nextTerm

            return leftTerm

        else:

            index = 0
            while index < len(self.operators):
                operator = self.operators[index]
                if (operator == "*"):
                    index += 1
                else:
                    leftTerm = self.evaluateTerm(self.items[index])
                    rightTerm = self.evaluateTerm(self.items[index + 1])
                    self.items[index] = leftTerm + rightTerm
                    self.operators.pop(index)
                    self.items.pop(index + 1)

            returner = 1
            for item in self.items:
                returner *= self.evaluateTerm(item)
            return returner
            

    def evaluateTerm(self, term) -> int:
        if isinstance(term, Expression):
            return term.evaluate()
        else:
            return term
        

day.run(part1, part2, 18)