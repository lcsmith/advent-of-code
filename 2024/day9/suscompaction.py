from itertools import repeat


EmptySpace = '.'

def run():
    disk_map = parse_input()
    actual_disk = unmap_disk_map(disk_map)

    compact_disk(actual_disk)
    checksum = calculate_checksum(actual_disk)
    print(checksum)


def calculate_checksum(actual_disk):
    checksum = 0
    for idx in range(0, len(actual_disk)):
        if actual_disk[idx] != EmptySpace:
            checksum += idx * actual_disk[idx]
    return checksum


def compact_disk(actual_disk):
    forward_idx = 0
    backward_idx = len(actual_disk)-1

    while forward_idx < backward_idx:
        if actual_disk[forward_idx] != EmptySpace:
            forward_idx += 1
        elif actual_disk[backward_idx] == EmptySpace:
            backward_idx -= 1
        else:
            actual_disk[forward_idx] = actual_disk[backward_idx]
            actual_disk[backward_idx] = EmptySpace
            forward_idx += 1
            backward_idx -= 1


def unmap_disk_map(disk_map):
    actual_disk = []
    for idx in range(0, len(disk_map)):
        repeat_count = int(disk_map[idx])
        if idx % 2 == 0:
            file_id = int(idx / 2)
            actual_disk += list(repeat(file_id, repeat_count))
        else:
            actual_disk += list(repeat(EmptySpace, repeat_count))
    return actual_disk


def parse_input():
    with open('input') as infile:
        return infile.read().strip()


if __name__ == '__main__':
    run()