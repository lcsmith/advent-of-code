def run(allow_dampening):
    line_levels = parse_input()

    safe_lines = 0
    for levels in line_levels:
        if are_levels_safe(levels, allow_dampening):
            safe_lines += 1

    print(safe_lines)

def parse_input():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    line_levels = [line.split(' ') for line in lines]
    line_levels = [[int(x) for x in line] for line in line_levels]
    return line_levels

def are_levels_safe(levels, allow_dampening):
    compare_next = [levels[x] - levels[x+1] for x in range(0,len(levels)-1)]
    if all(1 <= comp <= 3 for comp in compare_next) or all(-3 <= comp <= -1 for comp in compare_next):
        return True
    if allow_dampening:
        return any(are_levels_safe(subset, False) for subset in get_subsets(levels))
    return False

def get_subsets(levels):
    subsets = []
    for x in range(0, len(levels)):
        subsets.append(levels[:x] + levels[x+1:])
    return subsets

if __name__ == '__main__':
    run(False)
    run(True)
