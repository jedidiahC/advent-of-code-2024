def print_christmas_tree(width, height, robots, seconds_elapsed):
    map = []
    for _ in range(height):
        map.append(['.'] * width)

    for robot in robots:
        (position, velocity) = robot

        if map[position[1]][position[0]] == ".":
            map[position[1]][position[0]] = '1'
        else:
            map[position[1]][position[0]] = str(int('1') + 1)

    # Check symmetrical.
    line_threshold = 10
    line_count = 0
    for x in range(width):
        line_count = 0
        for y in range(1, height):
            if map[y][x] != '.' and map[y - 1][x] != '.':
                line_count += 1
                if line_count > line_threshold:
                    break
            else:
                line_count = 0

        if line_count > line_threshold:
            break

    if line_count < line_threshold:
        return

    with open("christmas.txt", "a", encoding="utf8") as output_file:
        output_file.write(str(seconds_elapsed))
        output = '\n'.join([''.join(row) for row in map])
        print(output)
        output_file.write(output)
        output_file.write("\n\n")


def solve(width, height, test_file, seconds, should_print=False):
    robots = []

    with open(f"../input/{test_file}", "r", encoding="utf-8") as input_file:
        for line in input_file:
            position, velocity = line.split(" ")[:2]
            position = list(map(int, position.split("=")[1].split(",")))
            velocity = list(map(int, velocity.split("=")[1].split(",")))

            robots.append((position, velocity))

    for current in range(seconds):
        for i, robot in enumerate(robots):
            robot = robots[i]
            (position, velocity) = robot
            new_position = [(position[0] + velocity[0]) %
                            width, (position[1] + velocity[1]) % height]
            robots[i] = (new_position, velocity)
        if should_print:
            print_christmas_tree(width, height, robots, current + 1)

    quadrants = {
        0: 0, 1: 0, 2: 0, 3: 0
    }

    for robot in robots:
        (position, _) = robot
        mid_width = int(width / 2)
        mid_height = int(height / 2)
        if position[0] < mid_width:
            if position[1] < mid_height:
                quadrants[0] += 1
            elif position[1] > mid_height:
                quadrants[1] += 1
        elif position[0] > mid_width:
            if position[1] < mid_height:
                quadrants[2] += 1
            elif position[1] > mid_height:
                quadrants[3] += 1

    score = 1
    for _, v in quadrants.items():
        score *= v

    print(score)


solve(11, 7, "14.test", 100)
solve(101, 103, "14.in", 100)
solve(101, 103, "14.in", 1000000, True)
