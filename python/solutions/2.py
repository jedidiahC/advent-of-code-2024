def are_levels_safe(levels):
    is_safe = True
    curr = 1
    direction = 1 if levels[1] - levels[0] > 0 else -1

    while curr < len(levels):
        a = levels[curr - 1]
        b = levels[curr]
        dist = abs(b - a)

        if (dist < 1 or dist > 3 or (b - a) / dist != direction):
            is_safe = False
            break

        curr += 1

    return is_safe

def solve_part_one():
    safe_reports = 0
    with open("2.in", "r") as input_file:
        for report in input_file:
            levels = [int(x) for x in report.split(" ")]
            safe_reports += 1 if are_levels_safe(levels) else 0

    print(safe_reports)

def solve_part_two():
    safe_reports = 0
    with open("2.in", "r") as input_file:
        for report in input_file:
            levels = [int(x) for x in report.split(" ")]
            is_safe = are_levels_safe(levels)

            to_remove = 0
            while not is_safe and to_remove < len(levels):
                test_level = levels.copy()
                test_level.pop(to_remove)
                is_safe = are_levels_safe(test_level)
                to_remove += 1

            safe_reports += 1 if is_safe else 0

    print(safe_reports)

solve_part_one()
solve_part_two()
