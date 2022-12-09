import os
import sys


def run_day9(num_knots):
    with open(os.path.join(sys.path[0], "day9\\input"), "r") as infile:
        lines = infile.readlines()

    knot_loc = [(0, 0)]*num_knots
    visited = set()

    for line in lines:
        movement = line.split()
        for step in range(int(movement[1])):
            knot_loc[0] = move_head(*knot_loc[0], movement[0])
            for knot in range(1, len(knot_loc)):
                knot_loc[knot] = move_trail(*knot_loc[knot-1], *knot_loc[knot])
            visited.add(knot_loc[num_knots-1])
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


def move_trail(lead_x, lead_y, trail_x, trail_y):
    if abs(trail_x-lead_x) == 2 and abs(trail_y-lead_y) == 2:
        return trail_x + (lead_x - trail_x)/2, trail_y + (lead_y - trail_y)/2
    if abs(trail_x - lead_x) == 2:
        return trail_x + (lead_x - trail_x)/2, lead_y
    if abs(trail_y-lead_y) == 2:
        return lead_x, trail_y + (lead_y - trail_y)/2
    return trail_x, trail_y
