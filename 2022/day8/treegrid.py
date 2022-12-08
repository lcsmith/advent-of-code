import os
import sys


def run_day8():
    with open(os.path.join(sys.path[0], "day8\\input"), "r") as infile:
        lines = infile.readlines()
    tree_heights = list(map(lambda x: [int(y) for y in x.strip()], lines))

    visibility = get_visibility(tree_heights)
    visible_trees = list(map(lambda t: [0]*len(t), tree_heights))

    for x in range(len(tree_heights[0])):
        for y in range(len(tree_heights)):
            if tree_heights[y][x] > visibility[y][x]:
                visible_trees[y][x] = 1

    return sum(map(lambda z: sum(z), visible_trees))


def get_visibility(tree_heights):
    left_visibility = list(map(lambda t: [-1]*len(t), tree_heights))
    for x in range(1, len(tree_heights[0])):
        for y in range(len(tree_heights)):
            left_visibility[y][x] = max(left_visibility[y][x-1], tree_heights[y][x-1])

    up_visibility = list(map(lambda t: [-1]*len(t), tree_heights))
    for x in range(len(tree_heights[0])):
        for y in range(1, len(tree_heights)):
            up_visibility[y][x] = max(up_visibility[y-1][x], tree_heights[y-1][x])

    right_visibility = list(map(lambda t: [-1]*len(t), tree_heights))
    for x in range(len(tree_heights[0])-2, -1, -1):
        for y in range(len(tree_heights)):
            right_visibility[y][x] = max(right_visibility[y][x+1], tree_heights[y][x+1])

    down_visibility = list(map(lambda t: [-1]*len(t), tree_heights))
    for x in range(len(tree_heights[0])):
        for y in range(len(tree_heights)-2, -1, -1):
            down_visibility[y][x] = max(down_visibility[y+1][x], tree_heights[y+1][x])

    visibility = list(map(lambda t: [0]*len(t), tree_heights))
    for x in range(len(tree_heights[0])):
        for y in range(len(tree_heights)):
            visibility[y][x] = min(left_visibility[y][x], right_visibility[y][x], up_visibility[y][x], down_visibility[y][x])

    return visibility
