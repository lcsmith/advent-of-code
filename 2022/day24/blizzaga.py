from collections import namedtuple

Location = namedtuple('Location', 'x y')
Blizzard = namedtuple('Blizzard', 'location direction')


def run():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    max_x = len(lines[0])-1
    max_y = len(lines)-1
    my_location = Location(0, lines[0].index('.'))
    target = Location(max_y, lines[-1].index('.'))

    blizzards = []
    for y in range(1, max_y):
        for x in range(1, max_x):
            if lines[y][x] != '.':
                blizzards.append(Blizzard(Location(x, y), lines[y][x]))

    time_blizzards = {0: blizzards}


def get_blizzards(time_blizzards, time, max_x, max_y):
    if time not in time_blizzards:
        previous_blizzards = get_blizzards(time_blizzards, time - 1, max_x, max_y)
        blizzards = [get_next(blizzard, max_x, max_y) for blizzard in previous_blizzards]
        time_blizzards[time] = blizzards

    return time_blizzards.get(time)


def get_next(blizzard, max_x, max_y):
    match blizzard.direction:
        case '>':
            next_location = Location(blizzard.location.x + 1, blizzard.location.y)
            if next_location.x >= max_x:
                next_location = Location(1, blizzard.location.y)
        case 'v':
            next_location = Location(blizzard.location.x, blizzard.location.y + 1)
            if next_location.y >= max_y:
                next_location = Location(blizzard.location.x, 1)
        case '<':
            next_location = Location(blizzard.location.x - 1, blizzard.location.y)
            if next_location.x <= 0:
                next_location = Location(max_x - 1, blizzard.location.y)
        case '^':
            next_location = Location(blizzard.location.x, blizzard.location.y - 1)
            if next_location.y <= 0:
                next_location = Location(blizzard.location.x, max_y - 1)
    return Blizzard(next_location, blizzard.direction)


if __name__ == '__main__':
    run()
