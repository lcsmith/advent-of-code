import re

def run_part1():
    with open('input') as infile:
        full_input = infile.read()

    matches = re.findall(r'mul\(([0-9]+),([0-9]+)\)', full_input)
    multiples = [int(x[0]) * int(x[1]) for x in matches]
    print(sum(multiples))


if __name__ == '__main__':
    run_part1()
