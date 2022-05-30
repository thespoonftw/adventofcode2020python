from common import day

def part1(lines) -> int: 
    return MessageVerifier(lines).solve()

def part2(lines) -> int:
    return 0

class MessageVerifier:

    def __init__(self, lines):

        self.rules = dict()
        self.messages = list()

        isReadingMessages = False
        for line in lines:

            if line == "":
                isReadingMessages = True

            elif isReadingMessages:
                self.messages.append(line)

            else:    
                split1 = line.split(": ")
                split2 = split1[1].split(" ")
                values = list()
                self.rules[int(split1[0])] = values

                if len(split2) == 1:
                    values.append(split2[0].replace('"', ''))                    

                elif len(split2) == 2:
                    values.append(int(split2[0]))
                    values.append(int(split2[1]))

                elif len(split2) == 3:
                    values.append(int(split2[0]))
                    values.append(split2[1])
                    values.append(int(split2[2]))

                elif len(split2) == 5:
                    values.append(int(split2[0]))
                    values.append(int(split2[1]))
                    values.append(split2[2])
                    values.append(int(split2[3]))
                    values.append(int(split2[4])) 


    def solve(self) -> int:
        return len([message for message in self.messages if self.isMessageValid(message)])

    def isMessageValid(self, message) -> bool:
        result = self.isMessageValidRecursive(message, self.rules[0], 0)
        returner = result[0] and result[1] == len(message)
        return returner

    def isMessageValidRecursive(self, message, rule, i) -> bool:
        # single letter rule
        if (len(rule) == 1):
            if message[i] == rule[0]:
                return True, 1
            else:
                return False, 1

        # two pointer rule
        elif (len(rule) == 2):
            result1 = self.isMessageValidRecursive(message, self.rules[rule[0]], i)
            result2 = self.isMessageValidRecursive(message, self.rules[rule[1]], i + result1[1])
            return result1[0] and result2[0], result1[1] + result2[1]

        elif (len(rule) == 3):
            result1 = self.isMessageValidRecursive(message, self.rules[rule[0]], i)
            result2 = self.isMessageValidRecursive(message, self.rules[rule[2]], i)
            return result1[0] or result2[0], result1[1]

        # four pointer rule
        elif (len(rule) == 5):
            result1 = self.isMessageValidRecursive(message, self.rules[rule[0]], i)
            result2 = self.isMessageValidRecursive(message, self.rules[rule[1]], i + result1[1])
            result3 = self.isMessageValidRecursive(message, self.rules[rule[3]], i)
            result4 = self.isMessageValidRecursive(message, self.rules[rule[4]], i + result3[1])
            resultBool = (result1[0] and result2[0]) or (result3[0] and result4[0])
            return resultBool, result1[1] + result2[1]

        x = 1

        

day.run(part1, part2, 19)