import os
import sys


def run_day3_part1():
    with open(os.path.join(sys.path[0], "day3\\input"), "r") as infile:
        lines = infile.readlines()

        total_priority = 0

        for line in lines:
            split_idx = int(len(line)/2)
            left_sack = set(line[:split_idx])
            right_sack = set(line[split_idx:])

            misplaced = left_sack.intersection(right_sack)
            total_priority += get_priority(misplaced.pop())

        return total_priority


def run_day3_part2():
    with open(os.path.join(sys.path[0], "day3\\input"), "r") as infile:
        lines = infile.readlines()

        total_priority = 0

        for triple_line in zip(*(iter(lines),) * 3):
            pack1 = set(triple_line[0].strip())
            pack2 = set(triple_line[1].strip())
            pack3 = set(triple_line[2].strip())

            badge = pack1.intersection(pack2).intersection(pack3)
            total_priority += get_priority(badge.pop())

        return total_priority


def get_priority(item):
    ascii_value = ord(item)
    if item.isupper():
        return ascii_value - 38
    return ascii_value - 96
