from collections import namedtuple

TableCoordinates = namedtuple('TableCoordinates', ['row', 'col'])
GardenPoint = namedtuple('GardenPoint', ['crop', 'location'])

North = TableCoordinates(-1,  0)
East  = TableCoordinates( 0,  1)
South = TableCoordinates( 1,  0)
West  = TableCoordinates( 0, -1)

def run():
    garden_map = parse_input()

    ungrouped_points = {}
    for row in range(len(garden_map)):
        for col in range(len(garden_map[0])):
            crop = garden_map[row][col]
            location = TableCoordinates(row, col)
            ungrouped_points[location] = GardenPoint(crop, location)

    regions = []
    while any(ungrouped_points):
        regions.append(build_region(ungrouped_points))

    total_result = sum([find_area(region) * find_perimeter(region) for region in regions])
    print(total_result)


def find_area(region):
    return len(region)

def find_perimeter(region):
    region_locations = {point.location for point in region}
    perimeter = 0
    for point in region_locations:
        for direction in [North, South, East, West]:
            adjacent_point = TableCoordinates(point.row + direction.row, point.col + direction.col)
            if adjacent_point not in region_locations:
                perimeter += 1
    return perimeter


    # Start with set of all individual points
    # Select first point in set, pull into new set
    # Find all matching adjacent points, remove from ungrouped,
    #   add to new set and add to "find all matching adjacent points"
def build_region(ungrouped_points):
    region_points = []
    popped_point = ungrouped_points.popitem()
    new_region_points = [popped_point[1]]
    while any(new_region_points):
        single_point = new_region_points.pop()
        for direction in [North, South, East, West]:
            adjacent_point = TableCoordinates(
                single_point.location.row + direction.row,
                single_point.location.col + direction.col)
            if adjacent_point in ungrouped_points and ungrouped_points[adjacent_point].crop == single_point.crop:
                popped_point = ungrouped_points.pop(adjacent_point)
                new_region_points.append(popped_point)
        region_points.append(single_point)

    return region_points


def parse_input():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    return [[x for x in line] for line in lines]


if __name__ == '__main__':
    run()