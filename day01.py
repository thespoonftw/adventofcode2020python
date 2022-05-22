from common import day

def part1(lines) -> int:    
    ints = list(map(int, lines))
    for a in ints:
        for b in ints:
            if (a + b == 2020):
                return a * b

def part2(lines) -> int:
    ints = list(map(int, lines))
    for a in ints:
        for b in ints:
            for c in ints:
                if (a + b + c == 2020):
                    return a * b * c

day.run(part1, part2, 1)
