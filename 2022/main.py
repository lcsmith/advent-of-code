from day1.calories import run_day1
from day2.rps import run_day2_part2, run_day2_part1
from day3.rucksack import run_day3_part1, run_day3_part2
from day4.cleaning import run_day4_part1, run_day4_part2
from day5.cratestack import run_day5_part1, run_day5_part2
from day6.signal import run_day6
from day7.directories import run_day7
from day8.treegrid import run_day8_part1, run_day8_part2
from day9.rope import run_day9


def run(day, part):
    match day, part:
        case 1, 1:
            return run_day1(1)
        case 1, 2:
            return run_day1(3)
        case 2, 1:
            return run_day2_part1()
        case 2, 2:
            return run_day2_part2()
        case 3, 1:
            return run_day3_part1()
        case 3, 2:
            return run_day3_part2()
        case 4, 1:
            return run_day4_part1()
        case 4, 2:
            return run_day4_part2()
        case 5, 1:
            return run_day5_part1()
        case 5, 2:
            return run_day5_part2()
        case 6, 1:
            return run_day6(4)
        case 6, 2:
            return run_day6(14)
        case 7, 1:
            return run_day7()
        case 7, 2:
            return run_day7()
        case 8, 1:
            return run_day8_part1()
        case 8, 2:
            return run_day8_part2()
        case 9, 1:
            return run_day9(2)
        case 9, 2:
            return run_day9(10)


if __name__ == '__main__':
    print(run(9, 2))
