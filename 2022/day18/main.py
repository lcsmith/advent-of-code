

def run():
    with open('input') as infile:
        lines = [line.strip() for line in infile]
    cubes = []
    for line in lines:
        x, y, z = line.split(",")
        cubes.append((int(x), int(y), int(z)))

    total_sides = 6 * len(cubes)
    for index in range(len(cubes)):
        for compare in range(index + 1, len(cubes)):
            if are_adjacent(cubes[index], cubes[compare]):
                total_sides -= 2
    print(total_sides)


def are_adjacent(cube1, cube2):
    same = 0
    one_away = 0
    for dimension in range(3):
        if cube1[dimension] == cube2[dimension]:
            same += 1
        if abs(cube1[dimension] - cube2[dimension]) == 1:
            one_away += 1
    return same == 2 and one_away == 1


if __name__ == '__main__':
    run()
