
class day:

    def read(path) -> list:

        data = open(path, 'r').read()
        return list(data.splitlines())
        

    def run(part1, part2, dayIndex):

        number = str(dayIndex).zfill(2)
        test = day.read("Input/test" + number + ".txt")
        input = day.read("Input/input" + number + ".txt")
        print(part1(test))
        print(part1(input))
        print(part2(test))
        print(part2(input))
