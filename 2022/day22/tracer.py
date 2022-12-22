import re


def run():
    facings = ['>', 'v', '<', '^']

    path, instructions = parse_input()

    facing_index = 0
    location_y = 1
    location_x = path[location_y].index('.')
    path[location_y][location_x] = facings[facing_index]

    for index in range(len(instructions)):
        instruction = instructions[index]
        if instruction.isnumeric():
            location_y, location_x = move_spaces(path, facings[facing_index], location_y, location_x, int(instruction))
        elif instruction == "R":
            facing_index = (facing_index + 1) % 4
            path[location_y][location_x] = facings[facing_index]
        elif instruction == "L":
            facing_index = (facing_index - 1) % 4
            path[location_y][location_x] = facings[facing_index]
        else:
            print("Huh?")

    print_path(path)
    print((1000 * location_y) + (4 * location_x) + facing_index)


def move_spaces(path, facing, location_y, location_x, spaces):
    match facing:
        case '>':
            step_y = 0
            step_x = 1
        case 'v':
            step_y = 1
            step_x = 0
        case '<':
            step_y = 0
            step_x = -1
        case '^':
            step_y = -1
            step_x = 0

    for step in range(spaces):
        next_y = location_y + step_y
        next_x = location_x + step_x
        if path[next_y][next_x] == ' ':
            backwards_y = -1 * step_y
            backwards_x = -1 * step_x
            next_y = location_y + backwards_y
            next_x = location_x + backwards_x
            while path[next_y][next_x] != ' ':
                next_y += backwards_y
                next_x += backwards_x
            next_y -= backwards_y
            next_x -= backwards_x
        if path[next_y][next_x] == '#':
            break
        location_y = next_y
        location_x = next_x
        path[location_y][location_x] = facing

    return location_y, location_x


def parse_input():
    with open('input') as infile:
        lines = [line[:-1] for line in infile]

    unpadded_path = [[char for char in line] for line in lines[:-2]]
    max_width = max([len(y) for y in unpadded_path])
    padded_path = [[' ']*(max_width+2)] + [[' '] + y + [' ']*(max_width-len(y)+1) for y in unpadded_path] + [[' ']*(max_width+2)]

    instruction_string = lines[-1:][0]
    instructions = re.findall("(\d+|L|R)", instruction_string)
    print(instructions)

    return padded_path, instructions


def print_path(path):
    to_print = []
    for y in range(len(path)):
        for x in range(len(path[y])):
            to_print.append(path[y][x])
        to_print.append("\n")
    print("".join(to_print))


if __name__ == '__main__':
    run()
