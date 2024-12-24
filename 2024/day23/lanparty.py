from collections import defaultdict


def run():
    connections = parse_input()

    connection_dict = build_connection_dict(connections)
    triplets = set()
    for computer in connection_dict:
        if computer.startswith('t'):
            for connected_computer in connection_dict[computer]:
                for third_connection in connection_dict[connected_computer]:
                    if third_connection in connection_dict[computer]:
                        triplets.add(frozenset({computer, connected_computer, third_connection}))
    print(len(triplets))

def build_connection_dict(connections):
    connection_dict = defaultdict(set)
    for connection in connections:
        connection_dict[connection[0]].add(connection[1])
        connection_dict[connection[1]].add(connection[0])
    return connection_dict


def parse_input():
    with open('input') as infile:
        return [line.strip().split('-') for line in infile]



if __name__ == '__main__':
    run()