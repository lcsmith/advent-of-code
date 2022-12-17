import itertools
import re
from functools import cmp_to_key

import networkx as nx


def run():
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
    shortest_paths = dict(nx.all_pairs_shortest_path(valves))
    unopened = list(flows.keys())
    for unopen in list(unopened):
        if flows[unopen] == 0:
            unopened.remove(unopen)

    best = 0
    for permute in itertools.permutations(unopened, 7):
        current = "AA"
        total_flow = 0
        time = 0
        my_permute = list(permute)
        my_unopened = list(unopened)
        while time < 30:
            if current in my_unopened:
                my_unopened.remove(current)
                time = time + 1
                total_flow = total_flow + (30 - time) * flows[current]
            elif my_unopened and my_permute:
                target = my_permute.pop()
                distance = len(shortest_paths[current][target]) - 1
                time = time + distance
                current = target
            else:
                time = time + 1
        best = max(best, total_flow)
    print(best)


if __name__ == '__main__':
    run()
