def run_part1():
    line_levels = parse_input()

    safe_lines = 0
    for levels in line_levels:
        is_increasing = levels[1] > levels[0]
        is_safe = True
        for x in range(1, len(levels)):
            if (levels[x] > levels[x-1]) != is_increasing:
                is_safe = False
            if not (1 <= abs(levels[x] - levels[x-1]) <= 3):
                is_safe = False
        if is_safe:
            safe_lines += 1

    print(safe_lines)

def parse_input():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    line_levels = [line.split(' ') for line in lines]
    line_levels = [[int(x) for x in line] for line in line_levels]
    return line_levels


if __name__ == '__main__':
    run_part1()
