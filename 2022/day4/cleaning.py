import os
import sys


def run_part1():
    return run_with_check(is_contained)


def run_part2():
    return run_with_check(is_overlapped)


def run_with_check(contain_or_overlap):
    with open(os.path.join(sys.path[0], "input"), "r") as infile:
        lines = infile.readlines()

    containments = 0

    for line in lines:
        assignments = line.split(",")
        first_range = assignments[0].split("-")
        second_range = assignments[1].split("-")
        if contain_or_overlap(first_range, second_range) | contain_or_overlap(second_range, first_range):
            containments += 1

    return containments


def is_contained(first, second):
    return int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1])


def is_overlapped(first, second):
    return int(first[0]) <= int(second[1]) and int(first[1]) >= int(second[0])


if __name__ == '__main__':
    print(run_part2())
