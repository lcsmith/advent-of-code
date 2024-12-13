from collections import namedtuple

TableCoordinates = namedtuple('TableCoordinates', ['row', 'col'])
LocationDirection = namedtuple('LocationDirection', ['location', 'direction'])

North = TableCoordinates(-1,  0)
East  = TableCoordinates( 0,  1)
South = TableCoordinates( 1,  0)
West  = TableCoordinates( 0, -1)

def run(include_blockers):
    map_chars = parse_input()
    guard_position = find_guard(map_chars)

    visited_states, _ = run_until_exit_or_loop(map_chars, guard_position)
    visited_locations = set([state.location for state in visited_states])

    print(len(visited_locations))

    if not include_blockers:
        return

    num_loopable = 0
    visited_locations.remove(guard_position)
    for location in visited_locations:
        map_chars[location.row][location.col] = 'O'
        new_path, did_exit = run_until_exit_or_loop(map_chars, guard_position)
        if not did_exit:
            num_loopable += 1
        map_chars[location.row][location.col] = '.'

    print(num_loopable)

def run_until_exit_or_loop(map_chars, guard_position):
    guard_direction = North
    location_direction = LocationDirection(guard_position, guard_direction)

    previous_states = set()

    while True:
        previous_states.add(location_direction)
        location_direction = take_step(map_chars, location_direction)
        if location_direction is None:
            return previous_states, True
        if location_direction in previous_states:
            return previous_states, False

def take_step(map_chars, location_direction):
    (guard_position, guard_direction) = location_direction

    next_position = TableCoordinates(
        guard_position.row + guard_direction.row, guard_position.col + guard_direction.col)
    if not 0 <= next_position.row < len(map_chars):
        return None
    if not 0 <= next_position.col < len(map_chars[0]):
        return None
    next_char = map_chars[next_position.row][next_position.col]
    if next_char == '#' or next_char == 'O':
        guard_direction = turn_right(guard_direction)
    else:
        guard_position = next_position
    return LocationDirection(guard_position, guard_direction)


def turn_right(guard_direction):
    if guard_direction == North:
        return East
    elif guard_direction == East:
        return South
    elif guard_direction == South:
        return West
    elif guard_direction == West:
        return North
    raise ValueError


def find_guard(map_chars):
    for row_idx in range(0, len(map_chars)):
        for col_idx in range(0, len(map_chars[0])):
            if map_chars[row_idx][col_idx] == '^':
                return TableCoordinates(row_idx, col_idx)


def print_map(map_chars):
    for row_idx in range(0, len(map_chars)):
        print(''.join(map_chars[row_idx]))


def parse_input():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    return [list(line) for line in lines]


if __name__ == '__main__':
    run(True)