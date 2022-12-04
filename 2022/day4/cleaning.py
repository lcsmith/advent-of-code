import os
import sys


def run_day4_part1():
    with open(os.path.join(sys.path[0], "day4\\input"), "r") as infile:
        lines = infile.readlines()

    containments = 0

    for line in lines:
        assignments = line.split(",")
        first_range = assignments[0].split("-")
        second_range = assignments[1].split("-")
        if is_contained(first_range, second_range) | is_contained(second_range, first_range):
            containments += 1

    return containments


def is_contained(first, second):
    return (int(first[0]) <= int(second[0])) & (int(first[1]) >= int(second[1]))
