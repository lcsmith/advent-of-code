

def run():
    with open('input') as infile:
        lines = [int(line.strip()) for line in infile]
    initial_ordering = dict([(x, lines[x]) for x in range(len(lines))])

    ring = [(x, lines[x]) for x in range(len(lines))]
    ring = do_mixing(initial_ordering, ring)

    zero_index = [x[1] for x in ring].index(0)
    zero_start = ring[zero_index:] + ring[:zero_index]
    print(zero_start[1000 % len(ring)][1] + zero_start[2000 % len(ring)][1] + zero_start[3000 % len(ring)][1])

    cipherkey = 811589153
    initial_ordering = dict([(x, lines[x] * cipherkey) for x in range(len(lines))])
    ring = [(x, lines[x] * cipherkey) for x in range(len(lines))]
    for mixing in range(10):
        ring = do_mixing(initial_ordering, ring)
    zero_index = [x[1] for x in ring].index(0)
    zero_start = ring[zero_index:] + ring[:zero_index]
    print(zero_start[1000 % len(ring)][1] + zero_start[2000 % len(ring)][1] + zero_start[3000 % len(ring)][1])


def do_mixing(initial_ordering, ring):
    for i in range(len(initial_ordering)):
        location = ring.index((i, initial_ordering[i]))
        ring = ring[location+1:] + ring[:location]
        target = initial_ordering[i] % (len(ring))
        ring = [(i, initial_ordering[i])] + ring[target:] + ring[:target]
    return ring


if __name__ == '__main__':
    run()
