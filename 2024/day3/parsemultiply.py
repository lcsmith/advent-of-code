import re

def run_part1():
    with open('input') as infile:
        full_input = infile.read()

    matches = re.findall(r'mul\(([0-9]+),([0-9]+)\)', full_input)
    multiples = [int(x[0]) * int(x[1]) for x in matches]
    print(sum(multiples))

def run_part2():
    with open('input') as infile:
        full_input = infile.read()

    sum_multiples = 0
    for match in re.finditer(r'mul\(([0-9]+),([0-9]+)\)', full_input):
        try:
            last_do = full_input.rindex("do()", 0, match.start())
        except ValueError:
            last_do = 0
        try:
            last_dont = full_input.rindex("don't()", 0, match.start())
        except ValueError:
            last_dont = 0
        if last_do >= last_dont:
            sum_multiples += int(match.group(1)) * int(match.group(2))
    print(sum_multiples)


if __name__ == '__main__':
    run_part1()
    run_part2()
