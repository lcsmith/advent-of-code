import os
import sys


def run():
    with open(os.path.join(sys.path[0], "input"), "r") as infile:
        lines = infile.readlines()

    cycle = 1
    register = 1
    registers = []
    strengths = []
    for line in lines:
        strengths.append(cycle*register)
        registers.append(register)
        cycle += 1
        if line != "noop\n":
            strengths.append(cycle*register)
            registers.append(register)
            cycle += 1
            instruction = line.split()
            register += int(instruction[1])

    return strengths[19]+strengths[59]+strengths[99]+strengths[139]+strengths[179]+strengths[219]


if __name__ == '__main__':
    print(run())
