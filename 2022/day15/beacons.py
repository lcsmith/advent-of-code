import re


def run_part1():
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
        distance = get_distance(sensor, beacon)
        for x in range(sensor[0] - distance, sensor[0] + distance):
            if get_distance(sensor, (x, important_y)) <= distance and (x, important_y) != beacon:
                exclusions.add((x, important_y))
    print(len(exclusions))


def run_part2():
    with open('input') as infile:
        lines = [line.strip() for line in infile]
    sensor_distances = []
    for line in lines:
        if not line:
            continue
        match = re.findall("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)[0]
        sensor = (int(match[0]), int(match[1]))
        beacon = (int(match[2]), int(match[3]))
        distance = get_distance(sensor, beacon)
        sensor_distances.append((sensor, distance))

    for y in range(0, 4000001):
        inclusions = [(0, 4000000)]
        exclusions = []
        for sensor_distance in sensor_distances:
            x_range = get_x_range(*sensor_distance, y)
            if x_range:
                exclusions.append(x_range)
        exclusions.sort()

        for exclusion in exclusions:
            for inclusion in inclusions.copy():
                if exclusion[0] > inclusion[1] or exclusion[1] < inclusion[0]:
                    continue

                inclusions.remove(inclusion)
                if exclusion[1] <= inclusion[1]:
                    inclusions.append((exclusion[1] + 1, inclusion[1]))
                if inclusion[0] <= exclusion[0]:
                    inclusions.append((inclusion[0], exclusion[0] - 1))

        if len(inclusions) == 1 and inclusions[0][0] == inclusions[0][1]:
            print((inclusions[0][0], y))


def get_x_range(sensor, distance, y):
    y_distance = abs(sensor[1] - y)
    remaining_distance = distance - y_distance
    if remaining_distance < 0:
        return None
    return sensor[0] - remaining_distance, sensor[0] + remaining_distance


def get_distance(point_a, point_b):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])


if __name__ == '__main__':
    run_part2()
