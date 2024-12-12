def solve():
    # Build grid.
    with open("../input/12.in", "r") as input_file:
        map = ["\n" + line for line in input_file]
        border = ["\n" * len(map[0])]
        map = border + map + border

    # Get components. each component must have pos and neighbours of diff type or border.
    visited = set()

    def get_plot_price(y, x, plant):
        queue = [(y, x)]
        fences = 0
        area = 0
        sides = {}

        while len(queue) > 0:
            current = queue.pop()

            if current in visited:
                continue

            visited.add(current)
            area += 1

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dir in directions:
                next = (current[0] + dir[0], current[1] + dir[1])

                if map[next[0]][next[1]] == plant:
                    if next in visited:
                        continue
                    queue.append(next)
                else:
                    fences += 1
                    side_id = current[0] if dir[0] != 0 else current[1]
                    if (dir + (side_id, )) not in sides:
                        sides[dir + (side_id, )] = set()

                    sides[dir + (side_id, )].add(next[1] if dir[0] != 0 else next[0])

        num_sides = 0

        for _, sides_group in sides.items():
            sides_list = sorted(sides_group)
            for index, value in enumerate(sides_list):
                if index == 0 or value != sides_list[index - 1] + 1:
                    num_sides += 1

        return fences * area, num_sides * area

    part_one, part_two = 0, 0
    for y in range(1, len(map) - 1):
        for x in range(1, len(map[0]) - 1):
            if (y, x) in visited or map[y][x] == "\n":
                continue
            fences_price, sides_price = get_plot_price(y, x, map[y][x])
            part_one += fences_price
            part_two += sides_price

    print(part_one, part_two)
solve()
