import re
from collections import namedtuple

Blueprint = namedtuple('Blueprint', 'number ore_ore clay_ore obsidian_ore obsidian_clay geode_ore geode_obsidian')
State = namedtuple('State', 'previous_state ore clay obsidian geode ore_robot clay_robot obsidian_robot geode_robot')


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

    is_part2 = True
    if is_part2:
        num_prints = 3
        total_time = 32
    else:
        num_prints = len(blueprints)
        total_time = 24

    quality_levels = []
    geodes = []

    for x in range(num_prints):
        best_geodes = get_best(blueprints[x], total_time)
        quality_levels.append(blueprints[x].number * best_geodes)
        geodes.append(best_geodes)
    print(sum(quality_levels))
    print(sum(geodes))


def get_best(blueprint, total_time):
    negative_state = State(previous_state=None, ore=0, clay=0, obsidian=0, geode=0, ore_robot=1, clay_robot=0,
                           obsidian_robot=0, geode_robot=0)
    starting_state = State(previous_state=negative_state, ore=0, clay=0, obsidian=0, geode=0, ore_robot=1, clay_robot=0,
                           obsidian_robot=0, geode_robot=0)
    states = [starting_state]
    for time in range(total_time):
        new_states = []
        for state in states:
            new_states += take_step(blueprint, state)
        states = new_states
    states.sort(key=lambda s: -1 * s.geode)
    print(states[0])
    return max([state.geode for state in states])


def take_step(blueprint, state):
    new_ore = state.ore + state.ore_robot
    new_clay = state.clay + state.clay_robot
    new_obsidian = state.obsidian + state.obsidian_robot
    new_geode = state.geode + state.geode_robot

    new_states = []

    if blueprint.geode_ore <= state.ore and blueprint.geode_obsidian <= state.obsidian:
        new_states.append(
            State(previous_state=state, ore=new_ore - blueprint.geode_ore, clay=new_clay,
                  obsidian=new_obsidian - blueprint.geode_obsidian, geode=new_geode, ore_robot=state.ore_robot,
                  clay_robot=state.clay_robot, obsidian_robot=state.obsidian_robot, geode_robot=state.geode_robot + 1))
        return new_states

    if True:
        new_states.append(
            State(previous_state=state, ore=new_ore, clay=new_clay, obsidian=new_obsidian, geode=new_geode, ore_robot=state.ore_robot,
                  clay_robot=state.clay_robot, obsidian_robot=state.obsidian_robot, geode_robot=state.geode_robot))

    if blueprint.ore_ore <= state.ore and \
            state.ore_robot < max(blueprint.ore_ore, blueprint.clay_ore, blueprint.obsidian_ore, blueprint.geode_ore) and \
            (did_build_last_state(state) or state.previous_state.ore < blueprint.ore_ore):
        new_states.append(
            State(previous_state=state, ore=new_ore - blueprint.ore_ore, clay=new_clay, obsidian=new_obsidian,
                  geode=new_geode, ore_robot=state.ore_robot + 1, clay_robot=state.clay_robot,
                  obsidian_robot=state.obsidian_robot, geode_robot=state.geode_robot))

    if blueprint.clay_ore <= state.ore and state.clay_robot < blueprint.obsidian_clay and \
            (did_build_last_state(state) or state.previous_state.ore < blueprint.clay_ore):
        new_states.append(
            State(previous_state=state, ore=new_ore - blueprint.clay_ore, clay=new_clay, obsidian=new_obsidian,
                  geode=new_geode, ore_robot=state.ore_robot, clay_robot=state.clay_robot + 1,
                  obsidian_robot=state.obsidian_robot, geode_robot=state.geode_robot))

    if blueprint.obsidian_ore <= state.ore and blueprint.obsidian_clay <= state.clay and \
            state.obsidian_robot < blueprint.geode_obsidian and \
            (did_build_last_state(state) or
             state.previous_state.ore < blueprint.obsidian_ore or
             state.previous_state.clay < blueprint.obsidian_clay):
        new_states.append(State(previous_state=state, ore=new_ore - blueprint.obsidian_ore,
                                clay=new_clay - blueprint.obsidian_clay, obsidian=new_obsidian, geode=new_geode,
                                ore_robot=state.ore_robot, clay_robot=state.clay_robot,
                                obsidian_robot=state.obsidian_robot + 1, geode_robot=state.geode_robot))

    return new_states


def did_build_last_state(state):
    return state.previous_state.ore_robot != state.ore_robot or \
        state.previous_state.clay_robot != state.clay_robot or \
        state.previous_state.obsidian_robot != state.obsidian_robot or \
        state.previous_state.geode_robot != state.geode_robot


if __name__ == '__main__':
    run()
