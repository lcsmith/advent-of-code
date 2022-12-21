import re
from collections import namedtuple

Blueprint = namedtuple('Blueprint', 'number ore_ore clay_ore obsidian_ore obsidian_clay geode_ore geode_obsidian')
State = namedtuple('State', 'ore clay obsidian geode ore_robot clay_robot obsidian_robot geode_robot')

def run():
    with open('input') as infile:
        lines = [line.strip() for line in infile]
    blueprints = []
    for line in lines:
        match = re.findall(
            "Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. "
            "Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.",
            line)[0]
        blueprints.append(Blueprint(*[int(m) for m in match]))

    quality_levels = []
    for blueprint in blueprints:
        best_geodes = get_best(blueprint)
        quality_levels.append(blueprint.number * best_geodes)
    print(sum(quality_levels))


def get_best(blueprint):
    states = [State(ore=0, clay=0, obsidian=0, geode=0, ore_robot=1, clay_robot=0, obsidian_robot=0, geode_robot=0)]
    for time in range(24):
        new_states = []
        for state in states:
            new_states += take_step(blueprint, state)
        states = new_states
    return max([state.geode for state in states])


def take_step(blueprint, state):
    new_ore = state.ore + state.ore_robot
    new_clay = state.clay + state.clay_robot
    new_obsidian = state.obsidian + state.obsidian_robot
    new_geode = state.geode + state.geode_robot

    new_states = [State(ore=new_ore, clay=new_clay, obsidian=new_obsidian, geode=new_geode, ore_robot=state.ore_robot, clay_robot=state.clay_robot, obsidian_robot=state.obsidian_robot, geode_robot=state.geode_robot)]
    # Fix hacky new-robot offset
    if state.ore < blueprint.ore_ore <= new_ore:
        new_states.append(State(ore=new_ore-blueprint.ore_ore-1, clay=new_clay, obsidian=new_obsidian, geode=new_geode, ore_robot=state.ore_robot+1, clay_robot=state.clay_robot, obsidian_robot=state.obsidian_robot, geode_robot=state.geode_robot))

    if state.ore < blueprint.clay_ore <= new_ore:
        new_states.append(State(ore=new_ore-blueprint.clay_ore, clay=new_clay-1, obsidian=new_obsidian, geode=new_geode, ore_robot=state.ore_robot, clay_robot=state.clay_robot+1, obsidian_robot=state.obsidian_robot, geode_robot=state.geode_robot))

    if blueprint.obsidian_ore <= new_ore and blueprint.obsidian_clay <= new_clay and (state.ore < blueprint.obsidian_ore or state.clay < blueprint.obsidian_clay):
        new_states.append(State(ore=new_ore-blueprint.obsidian_ore, clay=new_clay-blueprint.obsidian_clay, obsidian=new_obsidian-1, geode=new_geode, ore_robot=state.ore_robot, clay_robot=state.clay_robot, obsidian_robot=state.obsidian_robot+1, geode_robot=state.geode_robot))

    if blueprint.geode_ore <= new_ore and blueprint.geode_obsidian <= new_obsidian and (state.ore < blueprint.geode_ore or state.obsidian < blueprint.geode_obsidian):
        new_states.append(State(ore=new_ore-blueprint.geode_ore, clay=new_clay, obsidian=new_obsidian-blueprint.geode_obsidian, geode=new_geode-1, ore_robot=state.ore_robot, clay_robot=state.clay_robot, obsidian_robot=state.obsidian_robot, geode_robot=state.geode_robot+1))

    return new_states


if __name__ == '__main__':
    run()
