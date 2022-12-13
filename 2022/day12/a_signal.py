import heapq
import math
import os
import sys


def run():
    heights, start, target = parse_heights()

    traversal = list(map(lambda x: [None] * len(x), heights))
    print(traversal)
    traversal[start[0]][start[1]] = 0
    fringe = [apply_heuristic(start, 0, target)]
    heapq.heapify(fringe)
    while len(fringe) > 0:
        _, current_location = heapq.heappop(fringe)
        next_path_length = traversal[current_location[0]][current_location[1]]+1
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_step = try_take_step(heights, traversal, current_location, direction)
            if next_step is not None:
                if next_step == target:
                    print(next_path_length)
                    break
                traversal[next_step[0]][next_step[1]] = next_path_length
                heapq.heappush(fringe, apply_heuristic(next_step, next_path_length, target))


def apply_heuristic(location, path_length, target):
    estimate = math.sqrt(abs(location[0] - target[0])**2 + abs(location[1] - target[1])**2)
    return path_length + estimate, location


def try_take_step(heights, traversal, current_location, direction):
    maybe_next = (current_location[0]+direction[0], current_location[1]+direction[1])
    if not ((0 <= maybe_next[0] < len(heights)) and
            (0 <= maybe_next[1] < len(heights[0]))):
        return None
    if traversal[maybe_next[0]][maybe_next[1]] is not None:
        return None
    if heights[maybe_next[0]][maybe_next[1]] > (heights[current_location[0]][current_location[1]] + 1):
        return None

    return maybe_next


def parse_heights():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    heights = []
    for line_index in range(len(lines)):
        row = []
        heights.append(row)
        for char_index in range(len(lines[line_index])-1):
            if lines[line_index][char_index] == 'S':
                row.append(ord('a'))
                start = (line_index, char_index)
            elif lines[line_index][char_index] == 'E':
                row.append(ord('z'))
                target = (line_index, char_index)
            else:
                row.append(ord(lines[line_index][char_index]))
    return heights, start, target


if __name__ == '__main__':
    run()
