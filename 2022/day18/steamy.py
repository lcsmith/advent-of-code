

def run():
    with open('input') as infile:
        lines = [line.strip() for line in infile]
    cubes = []
    for line in lines:
        x, y, z = line.split(",")
        cubes.append((int(x), int(y), int(z)))

    min_edge = -1
    max_edge = 20
    steam = create_steam(cubes, min_edge, max_edge)
    steam_sides = get_all_sides(list(steam))
    exterior_length = max_edge - min_edge + 1
    print(steam_sides - 6 * exterior_length * exterior_length)


def get_all_sides(cubes):
    total_sides = 6 * len(cubes)
    for index in range(len(cubes)):
        for compare in range(index + 1, len(cubes)):
            if are_adjacent(cubes[index], cubes[compare]):
                total_sides -= 2
    return total_sides


def create_steam(cubes, min_edge, max_edge):
    cubes = set(cubes)
    steam = set([])
    expansion_set = set([(min_edge, min_edge, min_edge)])
    while expansion_set:
        steamlet = expansion_set.pop()
        if not (min_edge <= steamlet[0] <= max_edge and
                min_edge <= steamlet[1] <= max_edge and
                min_edge <= steamlet[2] <= max_edge):
            continue
        if steamlet in cubes or steamlet in steam:
            continue
        steam.add(steamlet)
        expansion_set.add((steamlet[0] + 1, steamlet[1], steamlet[2]))
        expansion_set.add((steamlet[0], steamlet[1] + 1, steamlet[2]))
        expansion_set.add((steamlet[0], steamlet[1], steamlet[2] + 1))
        expansion_set.add((steamlet[0] - 1, steamlet[1], steamlet[2]))
        expansion_set.add((steamlet[0], steamlet[1] - 1, steamlet[2]))
        expansion_set.add((steamlet[0], steamlet[1], steamlet[2] - 1))
    return steam


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
