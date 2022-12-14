

def run_part1():
    run_with_check(is_contained)


def run_part2():
    run_with_check(is_overlapped)


def run_with_check(contain_or_overlap):
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    containments = 0

    for line in lines:
        assignments = line.split(",")
        first_range = assignments[0].split("-")
        second_range = assignments[1].split("-")
        if contain_or_overlap(first_range, second_range) | contain_or_overlap(second_range, first_range):
            containments += 1

    print(containments)


def is_contained(first, second):
    return int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1])


def is_overlapped(first, second):
    return int(first[0]) <= int(second[1]) and int(first[1]) >= int(second[0])


if __name__ == '__main__':
    run_part2()
