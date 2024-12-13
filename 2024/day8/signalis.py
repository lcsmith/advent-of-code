from collections import namedtuple, defaultdict

TableCoordinates = namedtuple('TableCoordinates', ['row', 'col'])


def run_part1():
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
        for antinode in get_all_valid_antinodes(locations, row_length, col_length):
            antinodes.add(antinode)

    print(len(antinodes))
    #for antinode in antinodes:
    #    letter_grid[antinode.row][antinode.col] = '#'
    #print_map(letter_grid)


def get_all_valid_antinodes(locations, row_length, col_length):
    all_valid_antinodes = []

    for first_idx in range(0, len(locations)-1):
        for second_idx in range(first_idx+1, len(locations)):
            antinodes = get_antinodes(locations[first_idx], locations[second_idx])
            for antinode in antinodes:
                if 0 <= antinode.row < row_length and 0 <= antinode.col < col_length:
                    all_valid_antinodes.append(antinode)
    return all_valid_antinodes


def get_antinodes(first, second):
    row_diff = first.row - second.row
    col_diff = first.col - second.col

    first_antinode = TableCoordinates(first.row + row_diff, first.col + col_diff)
    second_antinode = TableCoordinates(second.row - row_diff, second.col - col_diff)
    return first_antinode, second_antinode


def print_map(map_chars):
    for row_idx in range(0, len(map_chars)):
        print(''.join(map_chars[row_idx]))


def parse_input():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    return [list(line) for line in lines]


if __name__ == '__main__':
    run_part1()
