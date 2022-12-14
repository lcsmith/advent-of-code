

def run():
    is_part2 = True
    cave = parse_cave(is_part2)
    sand_source = (500, 0)
    sand_particle = sand_source
    keep_dropping = True
    while keep_dropping:
        if sand_particle[1] >= 999:
            keep_dropping = False
        elif (cave[sand_particle[0]][sand_particle[1]+1]) == '.':
            sand_particle = sand_particle[0], sand_particle[1] + 1
        elif (cave[sand_particle[0]-1][sand_particle[1]+1]) == '.':
            sand_particle = sand_particle[0] - 1, sand_particle[1] + 1
        elif (cave[sand_particle[0]+1][sand_particle[1]+1]) == '.':
            sand_particle = sand_particle[0] + 1, sand_particle[1] + 1
        else:
            if sand_particle == sand_source:
                break
            cave[sand_particle[0]][sand_particle[1]] = 'o'
            sand_particle = sand_source
    print_cave(cave)


def parse_cave(is_part2):
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    cave = list(map(lambda z: ['.'] * 1000, range(1000)))
    deepest_y = 0
    for line in lines:
        path = line.split()
        path_segments = []
        for step in path:
            if step == "->":
                continue
            xy = [int(coordinate) for coordinate in step.split(",")]
            path_segments.append((xy[0], xy[1]))
            deepest_y = max(deepest_y, xy[1])

        for index in range(len(path_segments)-1):
            if path_segments[index][1] == path_segments[index+1][1]:
                start = min(path_segments[index][0], path_segments[index+1][0])
                end = max(path_segments[index][0], path_segments[index+1][0])
                for x in range(start, end+1):
                    cave[x][path_segments[index][1]] = '#'
            else:
                start = min(path_segments[index][1], path_segments[index+1][1])
                end = max(path_segments[index][1], path_segments[index+1][1])
                for y in range(start, end+1):
                    cave[path_segments[index][0]][y] = '#'
    if is_part2:
        for x in range(len(cave)):
            cave[x][deepest_y + 2] = "#"
    return cave


def print_cave(cave):
    cave_string = ""
    for y in range(len(cave[0])):
        for x in range(len(cave)):
            cave_string += cave[x][y]
        cave_string += "\n"
    print(cave_string)


if __name__ == '__main__':
    run()
