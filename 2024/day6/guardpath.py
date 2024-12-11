

def run():
    map_chars = parse_input()

    guard_position = find_guard(map_chars)
    guard_direction = [-1, 0]

    try:
        while True:
            take_step(map_chars, guard_position, guard_direction)
    except IndexError:
        pass

    visited_locations = 0
    for row_idx in range(0, len(map_chars)):
        for col_idx in range(0, len(map_chars[0])):
            if map_chars[row_idx][col_idx] == 'X':
                visited_locations += 1

    print(visited_locations)

    #print_map(map_chars)


def take_step(map_chars, guard_position, guard_direction):
    map_chars[guard_position[0]][guard_position[1]] = 'X'

    next_position = (guard_position[0] + guard_direction[0], guard_position[1] + guard_direction[1])
    next_char = map_chars[next_position[0]][next_position[1]]
    if next_char == '#':
        turn_right(guard_direction)
        pass
    else:
        guard_position[0] += guard_direction[0]
        guard_position[1] += guard_direction[1]


def turn_right(guard_direction):
    # [-1, 0] -> [0, 1] -> [1, 0] -> [0, -1]
    if guard_direction[0] != 0:
        guard_direction[1] = -1 * guard_direction[0]
        guard_direction[0] = 0
    else:
        swap = guard_direction[0]
        guard_direction[0] = guard_direction[1]
        guard_direction[1] = swap


def find_guard(map_chars):
    for row_idx in range(0, len(map_chars)):
        for col_idx in range(0, len(map_chars[0])):
            if map_chars[row_idx][col_idx] == '^':
                return [row_idx, col_idx]


def print_map(map_chars):
    for row_idx in range(0, len(map_chars)):
        print(''.join(map_chars[row_idx]))


def parse_input():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    return [list(line) for line in lines]


if __name__ == '__main__':
    run()