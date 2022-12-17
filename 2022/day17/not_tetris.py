

def run():
    with open('input') as infile:
        line = [line.strip() for line in infile][0]
    blows = [c for c in line]

    arena = list(map(lambda z: ['.'] * 7, range(3)))

    rocks = [[['#', '#', '#', '#']],
             [['.', '#', '.'], ['#', '#', '#'], ['.', '#', '.']],
             [['#', '#', '#'], ['.', '.', '#'], ['.', '.', '#']],
             [['#'], ['#'], ['#'], ['#']],
             [['#', '#'], ['#', '#']]]
    current_rock = rocks[0]
    rock_location = (2, 3)
    rock_count = 1
    step = 0
    while rock_count <= 2022:
        blow = blows[step % len(blows)]
        if blow == '<' and can_shift(arena, current_rock, *rock_location, -1, 0):
            rock_location = (rock_location[0] - 1, rock_location[1])
        elif blow == '>' and can_shift(arena, current_rock, *rock_location, 1, 0):
            rock_location = (rock_location[0] + 1, rock_location[1])

        if can_shift(arena, current_rock, *rock_location, 0, -1):
            rock_location = (rock_location[0], rock_location[1] - 1)
        else:
            place_rock(arena, current_rock, *rock_location)
            current_rock = rocks[rock_count % len(rocks)]
            rock_location = (2, 3 + get_max_height(arena))
            rock_count += 1
        step += 1

    print(current_rock)
    print(blow)
    print(rock_location)
    print_arena(arena)
    print(get_max_height(arena))


def get_max_height(arena):
    for y in range(len(arena)-1, -1, -1):
        if '#' in arena[y]:
            return y+1


def place_rock(arena, shape, location_x, location_y):
    extending_above = len(shape) + location_y - len(arena)
    if extending_above > 0:
        for extend in range(extending_above):
            arena.append(['.'] * 7)

    for x in range(len(shape[0])):
        for y in range(len(shape)):
            if shape[y][x] == '#':
                arena[location_y + y][location_x + x] = '#'


def can_shift(arena, shape, location_x, location_y, shift_x, shift_y):
    if location_x+shift_x <= -1 or location_x+shift_x+len(shape[0]) >= 8:
        return False
    if location_y + shift_y < 0:
        return False
    for x in range(len(shape[0])):
        for y in range(len(shape)):
            if (location_y+y+shift_y) >= len(arena):
                continue
            if shape[y][x] == '#' and arena[location_y+y+shift_y][location_x+x+shift_x] == '#':
                return False
    return True


def print_arena(arena):
    arena.reverse()
    printed = ""
    for row in arena:
        printed += "|"
        for column in row:
            printed += column
        printed += "|\n"
    printed += "+_______+"
    print(printed)


if __name__ == '__main__':
    run()
