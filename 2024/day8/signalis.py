from collections import namedtuple, defaultdict

TableCoordinates = namedtuple('TableCoordinates', ['row', 'col'])


def run(include_resonance):
    letter_grid = parse_input()

    antenna_locations = defaultdict(list)

    row_length = len(letter_grid)
    col_length = len(letter_grid[0])
    for row in range(0, row_length):
        for col in range(0, col_length):
            letter = letter_grid[row][col]
            if not letter == '.':
                antenna_locations[letter].append(TableCoordinates(row, col))

    antinodes = set()
    for freq in antenna_locations:
        locations = antenna_locations[freq]
        for antinode in get_all_valid_antinodes(locations, row_length, col_length, include_resonance):
            antinodes.add(antinode)

    print(len(antinodes))
    #for antinode in antinodes:
    #    letter_grid[antinode.row][antinode.col] = '#'
    #print_map(letter_grid)


def get_all_valid_antinodes(locations, row_length, col_length, include_resonance):
    all_valid_antinodes = []

    for first_idx in range(0, len(locations)-1):
        for second_idx in range(first_idx+1, len(locations)):
            antinodes = get_valid_antinodes(locations[first_idx], locations[second_idx], row_length, col_length, include_resonance)
            for antinode in antinodes:
                all_valid_antinodes.append(antinode)
    return all_valid_antinodes


def get_valid_antinodes(first, second, row_length, col_length, include_resonance):
    row_diff = first.row - second.row
    col_diff = first.col - second.col

    current_node = first
    while include_resonance or current_node == first:
        current_node = TableCoordinates(current_node.row + row_diff, current_node.col + col_diff)
        if is_valid(current_node, row_length, col_length):
            yield current_node
        else:
            break

    current_node = second
    while include_resonance or current_node == second:
        current_node = TableCoordinates(current_node.row - row_diff, current_node.col - col_diff)
        if is_valid(current_node, row_length, col_length):
            yield current_node
        else:
            break

    if include_resonance:
        yield first
        yield second


def is_valid(node, row_length, col_length):
    return 0 <= node.row < row_length and 0 <= node.col < col_length


def print_map(map_chars):
    for row_idx in range(0, len(map_chars)):
        print(''.join(map_chars[row_idx]))


def parse_input():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    return [list(line) for line in lines]


if __name__ == '__main__':
    run(False)
    run(True)
