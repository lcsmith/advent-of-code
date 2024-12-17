from collections import namedtuple


TableCoordinates = namedtuple('TableCoordinates', ['row', 'col'])

North = TableCoordinates(-1,  0)
East  = TableCoordinates( 0,  1)
South = TableCoordinates( 1,  0)
West  = TableCoordinates( 0, -1)

def run(deduplicate_paths):
    trail_map = parse_input()

    trailhead_values = get_all_trailhead_values(trail_map, deduplicate_paths)
    print(sum([value for trailhead, value in trailhead_values]))


def get_all_trailhead_values(trail_map, deduplicate_paths):
    trailheads = find_trailheads(trail_map)
    adjacency_map = build_adjacency_map(trail_map)
    trailhead_scores =\
        [(trailhead, get_trailhead_value(adjacency_map, trailhead, deduplicate_paths)) for trailhead in trailheads]
    return trailhead_scores


def get_trailhead_value(adjacency_map, trailhead, deduplicate_paths):
    accessible_locations = [trailhead]
    for elevation in range(9):
        next_accessible = []
        for location in accessible_locations:
            next_accessible.extend(adjacency_map[location.row][location.col])
        if deduplicate_paths:
            accessible_locations = list(set(next_accessible))
        else:
            accessible_locations = next_accessible
    return len(accessible_locations)


def build_adjacency_map(trail_map):
    adjacency_map = [[[] for _ in row] for row in trail_map]
    for row in range(0, len(trail_map)):
        for col in range(0, len(trail_map[0])):
            adjacency_map[row][col] = get_adjacencies(trail_map, TableCoordinates(row, col))
    return adjacency_map


def get_adjacencies(trail_map, current_location):
    current_height = trail_map[current_location.row][current_location.col]
    adjacencies = []
    for direction in [North, East, South, West]:
        adjacent_row = current_location.row + direction.row
        adjacent_col = current_location.col + direction.col
        if not 0 <= adjacent_row < len(trail_map):
            continue
        if not 0 <= adjacent_col < len(trail_map[0]):
            continue
        if trail_map[adjacent_row][adjacent_col] == current_height + 1:
            adjacencies.append(TableCoordinates(adjacent_row, adjacent_col))
    return adjacencies


def find_trailheads(trail_map):
    trailheads = []
    for row in range(0, len(trail_map)):
        for col in range(0, len(trail_map[0])):
            if trail_map[row][col] == 0:
                trailheads.append(TableCoordinates(row, col))
    return trailheads


def parse_input():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    return [[int(x) for x in line] for line in lines]


if __name__ == '__main__':
    run(True)
    run(False)