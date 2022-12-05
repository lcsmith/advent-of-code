import os
import sys


def run_day5_part1():
    with open(os.path.join(sys.path[0], "day5\\input"), "r") as infile:
        lines = infile.readlines()

        crates = [[] for _ in range(9)]
        handler = handle_initial_input
        for line in lines:
            handler = handler(line, crates)

        return [crate[0] for crate in crates]


def handle_initial_input(line, crates):
    if line[1] == "1":
        return handle_movement
    crate_index = 1
    while (crate_index <= 9) & ((crate_index*4 - 3) < len(line)):
        crate_name = line[crate_index*4 - 3]
        if crate_name.isalpha():
            crates[crate_index-1].append(crate_name)
        crate_index += 1
    return handle_initial_input


def handle_movement(line, crates):
    if line == "\n":
        return handle_movement
    instructions = line.split()
    num_to_move = int(instructions[1])
    source = int(instructions[3])-1
    destination = int(instructions[5])-1

    for _ in range(num_to_move):
        crate = crates[source].pop(0)
        crates[destination].insert(0, crate)
    return handle_movement
