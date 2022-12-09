import os
import sys


def run_day9_part1():
    with open(os.path.join(sys.path[0], "day9\\input"), "r") as infile:
        lines = infile.readlines()

    head_loc = (0, 0)
    tail_loc = (0, 0)
    visited = set()

    for line in lines:
        movement = line.split()
        for step in range(int(movement[1])):
            head_loc = move_head(*head_loc, movement[0])
            tail_loc = move_tail(*head_loc, *tail_loc)
            visited.add(tail_loc)

    return len(visited)


def move_head(x, y, direction):
    match direction:
        case "U":
            return x, y+1
        case "D":
            return x, y-1
        case "L":
            return x-1, y
        case "R":
            return x+1, y


def move_tail(head_x, head_y, tail_x, tail_y):
    if tail_x == head_x + 2:
        return tail_x - 1, head_y
    if tail_x == head_x - 2:
        return tail_x + 1, head_y
    if tail_y == head_y + 2:
        return head_x, tail_y - 1
    if tail_y == head_y - 2:
        return head_x, tail_y + 1
    return tail_x, tail_y
