
def solve_part_one(width, height, test_file):
    robots = []

    with open(f"../input/{test_file}", "r", encoding="utf-8") as input_file:
        for line in input_file:
            position, velocity = line.split(" ")[:2]
            position = list(map(int, position.split("=")[1].split(",")))
            velocity = list(map(int, velocity.split("=")[1].split(",")))

            robots.append((position, velocity))

    for _ in range(100):
        for i, robot in enumerate(robots):
            robot = robots[i]
            (position, velocity) = robot
            new_position = [(position[0] + velocity[0]) %
                            width, (position[1] + velocity[1]) % height]
            robots[i] = (new_position, velocity)

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


solve_part_one(11, 7, "14.test")
solve_part_one(101, 103, "14.in")
