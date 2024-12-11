

def run_part1():
    letter_grid = parse_input()

    total_xmas = 0
    for row_idx in range(0, len(letter_grid)):
        for col_idx in range(0, len(letter_grid[0])):
            total_xmas += find_xmas_count(letter_grid, row_idx, col_idx)
    print(total_xmas)

def find_xmas_count(letter_grid, row_idx, col_idx):
    if letter_grid[row_idx][col_idx] != 'X':
        return 0
    xmas_count = 0
    for row_dir in [-1,0,1]:
        for col_dir in [-1,0,1]:
            if row_dir == 0 and col_dir == 0:
                continue
            if is_xmas(letter_grid, row_idx, col_idx, row_dir, col_dir):
                xmas_count += 1
    return xmas_count

def is_xmas(letter_grid, row_idx, col_idx, row_dir, col_dir):
    if not 0 <= (row_idx + 3*row_dir) < len(letter_grid):
        return False
    if not 0 <= (col_idx + 3*col_dir) < len(letter_grid[0]):
        return False
    if letter_grid[row_idx + row_dir][col_idx + col_dir] != 'M':
        return False
    if letter_grid[row_idx + 2*row_dir][col_idx + 2*col_dir] != 'A':
        return False
    if letter_grid[row_idx + 3*row_dir][col_idx + 3*col_dir] != 'S':
        return False
    return True

def run_part2():
    letter_grid = parse_input()

    total_x_mas = 0
    for row_idx in range(1, len(letter_grid)-1):
        for col_idx in range(1, len(letter_grid[0])-1):
            if is_x_mas(letter_grid, row_idx, col_idx):
                total_x_mas += 1
    print(total_x_mas)

def is_x_mas(letter_grid, row_idx, col_idx):
    if letter_grid[row_idx][col_idx] != 'A':
        return False
    upper_left  = letter_grid[row_idx-1][col_idx-1]
    upper_right = letter_grid[row_idx+1][col_idx-1]
    lower_left  = letter_grid[row_idx-1][col_idx+1]
    lower_right = letter_grid[row_idx+1][col_idx+1]

    if not (upper_left == 'M' and lower_right == 'S' or upper_left == 'S' and lower_right == 'M'):
        return False
    if not (upper_right == 'M' and lower_left == 'S' or upper_right == 'S' and lower_left == 'M'):
        return False

    return True

def parse_input():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    return [list(line) for line in lines]


if __name__ == '__main__':
    run_part1()
    run_part2()
