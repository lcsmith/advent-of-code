import os
import sys


def run_day1(num_elves):
    with open(os.path.join(sys.path[0], "day1\\input"), "r") as infile:
        lines = infile.readlines()

    best_calories = [0]*num_elves
    current_calories = 0

    for line in lines:
        if line.isspace():
            if current_calories > best_calories[0]:
                best_calories[0] = current_calories
                best_calories.sort()
            current_calories = 0
        else:
            current_calories += int(line)

    return sum(best_calories)
