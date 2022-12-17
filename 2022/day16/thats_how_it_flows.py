import itertools
import re
import matplotlib.pyplot as plt
import networkx as nx


def run():
    valves, flows = parse_graph()

    visualize = False
    if visualize:
        nx.draw(valves, with_labels=True)
        plt.show()
        return

    shortest_paths = dict(nx.all_pairs_shortest_path(valves))
    unopened = [valve for valve in flows.keys() if flows[valve] != 0]

    # Just kinda eyeball it, this looks like the right division
    unopened_1 = ['KL', 'YS', 'CD', 'ID', 'AC', 'MJ', 'BO', 'KW', 'DT']
    unopened_2 = ['OU', 'DY', 'RH', 'DI', 'TO', 'OI']

    print(get_best(shortest_paths, flows, unopened, 30, 7))
    print(get_best(shortest_paths, flows, unopened_1, 26, len(unopened_1)) +
          get_best(shortest_paths, flows, unopened_2, 26, len(unopened_2)))


def get_best(shortest_paths, flows, unopened, total_time, choose):
    best = 0
    for permute in itertools.permutations(unopened, choose):
        current = "AA"
        total_flow = 0
        time = 0
        my_permute = list(permute)
        my_unopened = list(unopened)
        while time < total_time:
            if current in my_unopened:
                my_unopened.remove(current)
                time = time + 1
                total_flow = total_flow + (total_time - time) * flows[current]
            elif my_unopened and my_permute:
                target = my_permute.pop()
                distance = len(shortest_paths[current][target]) - 1
                time = time + distance
                current = target
            else:
                time = time + 1
        best = max(best, total_flow)
    return best


def parse_graph():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    valves = nx.Graph()
    flows = {}
    for line in lines:
        match = re.findall("Valve ([A-Z]+) has flow rate=(-?\d+); tunnels? leads? to valves? (.*)$", line)[0]
        valve = match[0]

        flow_rate = int(match[1])
        flows[valve] = flow_rate

        connections = match[-1].split(",")
        valves.add_node(valve)
        for connection in connections:
            valves.add_edge(valve, connection.strip())
    return valves, flows


if __name__ == '__main__':
    run()
