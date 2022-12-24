from collections import namedtuple

Location = namedtuple('Location', 'x y')

def run():
    with open('input') as infile:
        lines = [line.strip() for line in infile]
    elves = set()
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (lines[y][x]) == '#':
                elves.add(Location(x, y))

    ordered_steps = list(range(4))

    for time in range(10):
        proposals = {}
        for elf_location in list(elves):
            proposal = get_proposal(elves, elf_location, ordered_steps)
            if proposal is not None:
                if proposal in proposals:
                    proposals[proposal] = None
                else:
                    proposals[proposal] = elf_location
        for proposal in proposals:
            if proposals[proposal] is not None:
                elves.remove(proposals[proposal])
                elves.add(proposal)
        ordered_steps.append(ordered_steps.pop(0))

    min_x = min([elf.x for elf in elves])
    max_x = max([elf.x for elf in elves])
    min_y = min([elf.y for elf in elves])
    max_y = max([elf.y for elf in elves])
    print((max_x - min_x + 1) * (max_y - min_y + 1) - len(elves))
            

def get_proposal(elves, location, ordered_steps):
    good_steps = []
    for step in ordered_steps:
        if step == 0:
            maybe_next = Location(location.x, location.y - 1)
            first_open = Location(location.x + 1, location.y - 1)
            second_open = Location(location.x - 1, location.y - 1)
        elif step == 1:
            maybe_next = Location(location.x, location.y + 1)
            first_open = Location(location.x + 1, location.y + 1)
            second_open = Location(location.x - 1, location.y + 1)
        elif step == 2:
            maybe_next = Location(location.x - 1, location.y)
            first_open = Location(location.x - 1, location.y + 1)
            second_open = Location(location.x - 1, location.y - 1)
        elif step == 3:
            maybe_next = Location(location.x + 1, location.y)
            first_open = Location(location.x + 1, location.y + 1)
            second_open = Location(location.x + 1, location.y - 1)

        if maybe_next not in elves and first_open not in elves and second_open not in elves:
            good_steps.append(maybe_next)

    if len(good_steps) in (0, 4):
        return None
    return good_steps[0]


if __name__ == '__main__':
    run()
