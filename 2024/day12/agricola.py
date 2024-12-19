from collections import namedtuple
from common import table_map as tm

GardenPoint = namedtuple('GardenPoint', ['crop', 'location'])

def run():
    garden_map = parse_input()

    ungrouped_points = {}
    for row in range(len(garden_map)):
        for col in range(len(garden_map[0])):
            crop = garden_map[row][col]
            location = tm.TableCoordinates(row, col)
            ungrouped_points[location] = GardenPoint(crop, location)

    regions = []
    while any(ungrouped_points):
        regions.append(build_region(ungrouped_points))

    total_result = sum([find_area(region) * find_perimeter(region) for region in regions])
    print(total_result)

    total_result = sum([find_area(region) * find_sides(region) for region in regions])
    print(total_result) # 693589 too low


def find_area(region):
    return len(region)

def find_perimeter(region):
    region_locations = {point.location for point in region}
    perimeter = 0
    for point in region_locations:
        for direction in tm.CardinalDirections:
            adjacent_point = tm.add_coordinates(point, direction)
            if adjacent_point not in region_locations:
                perimeter += 1
    return perimeter

def find_sides(region):
    region_locations = {point.location for point in region}
    maybe_sides = {tm.LocationDirection(location, direction)
                   for direction in tm.CardinalDirections
                   for location in region_locations}
    for location_direction in list(maybe_sides):
        adjacent = tm.traverse_location_direction(location_direction)
        if adjacent in region_locations:
            maybe_sides.remove(location_direction)
    # pop a maybe_side point+direction. Check each perpendicular direction -
    #   if adjacent is in the region, and adjacent+direction is in maybe_sides, they're part of the same side.
    # Pop that too and continue checking
    num_sides = 0
    while any(maybe_sides):
        num_sides += 1
        side_seed = maybe_sides.pop()
        for perp in get_perpendiculars(side_seed.direction):
            side_next_loc = side_seed.location
            while side_next_loc in region_locations:
                side_next_loc = tm.add_coordinates(side_next_loc, perp)
                maybe_same_side = tm.LocationDirection(side_next_loc, side_seed.direction)
                if maybe_same_side in maybe_sides:
                    maybe_sides.remove(maybe_same_side)
                else:
                    break
    return num_sides


def get_perpendiculars(direction):
    if direction in [tm.North, tm.South]:
        return [tm.East, tm.West]
    if direction in [tm.East, tm.West]:
        return [tm.North, tm.South]
    raise ValueError


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
        for direction in tm.CardinalDirections:
            adjacent_point = tm.add_coordinates(single_point.location, direction)
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