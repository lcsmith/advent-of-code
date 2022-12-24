import heapq
import math
from collections import namedtuple

Location = namedtuple('Location', 'x y')
Blizzard = namedtuple('Blizzard', 'location direction')
Temporal = namedtuple('Temporal', 'location time')


def run():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    max_x = len(lines[0])-1
    max_y = len(lines)-1
    start = Location(lines[0].index('.'), 0)
    target = Location(lines[-1].index('.'), max_y)

    blizzards = {}
    for y in range(1, max_y):
        for x in range(1, max_x):
            if lines[y][x] != '.':
                blizzards[Location(x, y)] = [lines[y][x]]

    time_blizzards = {0: blizzards}
    first_time = get_astar_time(time_blizzards, 0, start, target, max_x, max_y)
    print(first_time)
    second_time = get_astar_time(time_blizzards, first_time, target, start, max_x, max_y)
    third_time = get_astar_time(time_blizzards, second_time, start, target, max_x, max_y)
    print(third_time)


def get_astar_time(time_blizzards, initial_time, start, target, max_x, max_y):
    visited = {Temporal(start, initial_time)}
    fringe = [apply_heuristic(Temporal(start, initial_time), target)]
    heapq.heapify(fringe)
    while len(fringe) > 0:
        _, temporal = heapq.heappop(fringe)
        next_time = temporal.time + 1
        current_blizzards = get_blizzards(time_blizzards, next_time, max_x, max_y)
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
            next_step = Location(temporal.location.x + direction[0], temporal.location.y + direction[1])
            if next_step == target:
                return next_time
            if 0 < next_step.x < max_x and 0 < next_step.y < max_y and next_step not in current_blizzards or \
                    next_step == start:
                next_temporal = Temporal(next_step, next_time)
                if next_temporal not in visited:
                    visited.add(next_temporal)
                    heapq.heappush(fringe, apply_heuristic(next_temporal, target))


def apply_heuristic(temporal, target):
    estimate = math.sqrt(abs(temporal.location.x - target.x)**2 + abs(temporal.location.y - target.y)**2)
    return temporal.time + estimate, temporal


def get_blizzards(time_blizzards, time, max_x, max_y):
    if time not in time_blizzards:
        previous_blizzards = get_blizzards(time_blizzards, time - 1, max_x, max_y)
        blizzards = {}
        for blizzard in previous_blizzards:
            for direction in previous_blizzards[blizzard]:
                next_location = get_next_blizzard_location(blizzard, direction, max_x, max_y)
                if next_location in blizzards:
                    blizzards[next_location].append(direction)
                else:
                    blizzards[next_location] = [direction]
        time_blizzards[time] = blizzards

    return time_blizzards.get(time)


def get_next_blizzard_location(location, direction, max_x, max_y):
    match direction:
        case '>':
            next_location = Location(location.x + 1, location.y)
            if next_location.x >= max_x:
                next_location = Location(1, location.y)
        case 'v':
            next_location = Location(location.x, location.y + 1)
            if next_location.y >= max_y:
                next_location = Location(location.x, 1)
        case '<':
            next_location = Location(location.x - 1, location.y)
            if next_location.x <= 0:
                next_location = Location(max_x - 1, location.y)
        case '^':
            next_location = Location(location.x, location.y - 1)
            if next_location.y <= 0:
                next_location = Location(location.x, max_y - 1)
    return next_location


if __name__ == '__main__':
    run()
