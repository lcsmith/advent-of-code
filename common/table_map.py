from collections import namedtuple

TableCoordinates = namedtuple('TableCoordinates', ['row', 'col'])
LocationDirection = namedtuple('LocationDirection', ['location', 'direction'])

North = TableCoordinates(-1,  0)
East  = TableCoordinates( 0,  1)
South = TableCoordinates( 1,  0)
West  = TableCoordinates( 0, -1)

CardinalDirections = {North, South, East, West}

def add_coordinates(left, right):
    return TableCoordinates(left.row + right.row, left.col + right.col)

def traverse_location_direction(location_direction):
    return add_coordinates(location_direction.location, location_direction.direction)