def run():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    line_split = [line.split('   ') for line in lines]
    first_list = [int(split_line[0]) for split_line in line_split]
    second_list = [int(split_line[1]) for split_line in line_split]

    first_list.sort()
    second_list.sort()

    total_distance = 0
    for x in range(0, len(line_split)):
        total_distance += abs(first_list[x] - second_list[x])

    print(total_distance)

if __name__ == '__main__':
    run()
