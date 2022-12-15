import re
import math


def run():
    with open('input') as infile:
        lines = [line.strip() for line in infile]
    exclusions = set([])
    important_y = 2000000
    for line in lines:
        if not line:
            continue
        match = re.findall("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)[0]
        sensor = (int(match[0]), int(match[1]))
        beacon = (int(match[2]), int(match[3]))
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        for x in range(sensor[0] - distance, sensor[0] + distance):
            if get_distance(sensor, (x, important_y)) <= distance and (x, important_y) != beacon:
                exclusions.add((x, important_y))
    print(len(exclusions))


def get_distance(pointA, pointB):
    return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])


if __name__ == '__main__':
    run()
