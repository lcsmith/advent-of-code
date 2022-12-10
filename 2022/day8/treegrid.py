import os
import sys


def run_part1():
    with open(os.path.join(sys.path[0], "day8\\input"), "r") as infile:
        lines = infile.readlines()
    tree_heights = list(map(lambda x: [int(y) for y in x.strip()], lines))

    visibility = get_visibility(tree_heights)
    visible_trees = list(map(lambda t: [0]*len(t), tree_heights))

    for x in range(len(tree_heights[0])):
        for y in range(len(tree_heights)):
            if tree_heights[y][x] > visibility[y][x]:
                visible_trees[y][x] = 1

    print(sum(map(lambda z: sum(z), visible_trees)))


def run_part2():
    with open(os.path.join(sys.path[0], "input"), "r") as infile:
        lines = infile.readlines()
    tree_heights = list(map(lambda x: [int(y) for y in x.strip()], lines))

    view_scores = get_view_distance(tree_heights)

    print(max(map(max, view_scores)))


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


def get_view_distance(tree_heights):
    view_scores = list(map(lambda t: [0]*len(t), tree_heights))
    for x in range(len(tree_heights[0])):
        for y in range(len(tree_heights)):
            view_scores[y][x] = direction_distance(tree_heights, x, y, lambda xx, yy: (xx-1, yy)) * \
                                direction_distance(tree_heights, x, y, lambda xx, yy: (xx, yy-1)) * \
                                direction_distance(tree_heights, x, y, lambda xx, yy: (xx+1, yy)) * \
                                direction_distance(tree_heights, x, y, lambda xx, yy: (xx, yy+1))
    return view_scores


def direction_distance(tree_heights, x, y, position_mover):
    base_height = tree_heights[y][x]

    total_distance = 0
    x, y = position_mover(x, y)
    while 0 <= x < len(tree_heights[0]) and 0 <= y < len(tree_heights):
        total_distance += 1
        if tree_heights[y][x] >= base_height:
            return total_distance
        x, y = position_mover(x, y)

    return total_distance


if __name__ == '__main__':
    run_part2()
