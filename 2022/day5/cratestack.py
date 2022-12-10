import os
import sys


def run_part1():
    run_with_movement_handler(one_at_a_time)


def run_part2():
    run_with_movement_handler(all_at_once)


def run_with_movement_handler(crane):
    with open(os.path.join(sys.path[0], "input"), "r") as infile:
        lines = infile.readlines()

        crates = [[] for _ in range(9)]
        handler = handle_initial_input
        for line in lines:
            handler = handler(line, crates, crane)

        print([crate[0] for crate in crates])


def handle_initial_input(line, crates, _):
    if line[1] == "1":
        return handle_movement
    crate_index = 1
    while crate_index <= 9 and (crate_index*4 - 3) < len(line):
        crate_name = line[crate_index*4 - 3]
        if crate_name.isalpha():
            crates[crate_index-1].append(crate_name)
        crate_index += 1
    return handle_initial_input


def handle_movement(line, crates, crane):
    if line == "\n":
        return handle_movement
    instructions = line.split()
    num_to_move = int(instructions[1])
    source_index = int(instructions[3])-1
    destination_index = int(instructions[5])-1

    crane(num_to_move, crates[source_index], crates[destination_index])

    return handle_movement


def one_at_a_time(num_to_move, source, destination):
    for _ in range(num_to_move):
        crate = source.pop(0)
        destination.insert(0, crate)


def all_at_once(num_to_move, source, destination):
    for index in range(num_to_move):
        crate = source.pop(0)
        destination.insert(index, crate)


if __name__ == '__main__':
    run_part2()
