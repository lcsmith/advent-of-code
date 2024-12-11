def run_part1():
    letter_grid = parse_input()

    total_xmas = 0
    for col_idx in range(0, len(letter_grid)):
        for row_idx in range(0, len(letter_grid[0])):
            total_xmas += find_xmas_count(letter_grid, col_idx, row_idx)
    print(total_xmas)

def find_xmas_count(letter_grid, col_idx, row_idx):
    if letter_grid[col_idx][row_idx] != 'X':
        return 0
    xmas_count = 0
    for col_dir in [-1,0,1]:
        for row_dir in [-1,0,1]:
            if col_dir == 0 and row_dir == 0:
                continue
            if is_xmas(letter_grid, col_idx, row_idx, col_dir, row_dir):
                xmas_count += 1
    return xmas_count

def is_xmas(letter_grid, col_idx, row_idx, col_dir, row_dir):
    if not 0 <= (col_idx + 3*col_dir) < len(letter_grid):
        return False
    if not 0 <= (row_idx + 3*row_dir) < len(letter_grid[0]):
        return False
    if letter_grid[col_idx + col_dir][row_idx + row_dir] != 'M':
        return False
    if letter_grid[col_idx + 2*col_dir][row_idx + 2*row_dir] != 'A':
        return False
    if letter_grid[col_idx + 3*col_dir][row_idx + 3*row_dir] != 'S':
        return False
    return True


def parse_input():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    return [list(line) for line in lines]


if __name__ == '__main__':
    run_part1()
