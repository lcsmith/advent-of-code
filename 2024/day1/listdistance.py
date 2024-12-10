def run_part1():
    first_list, second_list = parse_input()

    first_list.sort()
    second_list.sort()

    total_distance = 0
    for x in range(0, len(first_list)):
        total_distance += abs(first_list[x] - second_list[x])

    print(total_distance)

def run_part2():
    first_list, second_list = parse_input()

    total_similarity = 0
    for x in range(0, len(first_list)):
        total_similarity += first_list[x] * second_list.count(first_list[x])

    print(total_similarity)

def parse_input():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    line_split = [line.split('   ') for line in lines]
    first_list = [int(split_line[0]) for split_line in line_split]
    second_list = [int(split_line[1]) for split_line in line_split]

    return first_list, second_list


if __name__ == '__main__':
    run_part1()
    run_part2()
