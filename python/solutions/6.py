def build_level():
    map = []
    with open("6.in", "r") as input_file:
        row_index = 0
        for line in input_file:
            row = []
            col_index = 0
            for c in line:
                row.append(c)
                if c == '^':
                    guard_pos = (row_index, col_index)
                col_index += 1
            row_index += 1
            map.append(row)

    return (map, guard_pos)


def solve():
    (map, guard_pos) = build_level()

    def is_in_map(pos):
        return pos[0] > -1 and pos[0] < len(map) and pos[1] > -1 and pos[1] < len(map[0])
    def add(a, b):
        return (a[0] + b[0], a[1] + b[1])
    def at(pos):
        return map[pos[0]][pos[1]]
    def update(pos, c):
        map[pos[0]][pos[1]] = c
    def rotate_dir(curr_dir):
        return (curr_dir[1], -curr_dir[0])
    def get_footprint(pos, dir):
        return (pos[0], pos[1], dir[0], dir[1])

    visited = set()
    footprints = set()

    guard_dir = (-1, 0)

    possible_obstructions = 0
    while is_in_map(guard_pos):
        visited.add(guard_pos)
        footprints.add(get_footprint(guard_pos, guard_dir))

        if at(guard_pos) != 'O' and at(guard_pos) != '+':
            update(guard_pos, '|' if guard_dir[0] != 0 else '-')

        next_pos = add(guard_pos, guard_dir)

        # Rotate guard.
        while is_in_map(next_pos) and at(next_pos) == '#':
            guard_dir = rotate_dir(guard_dir)
            next_pos = add(guard_pos, guard_dir)
            if at(guard_pos) != 'O':
                update(guard_pos, '+')

        # Check if can place obstruction at next pos. Ensure we don't put the obstacle where guard has already travelled.
        obstacle_pos = next_pos
        if obstacle_pos not in visited and is_in_map(obstacle_pos) and at(obstacle_pos) != '#':
            # Store a "footprint" of guard dirs after visiting a tile.
            redirect_footprints = footprints.copy()

            redirect_dir = guard_dir
            redirect_pos = guard_pos

            # Start moving from current pos.
            while is_in_map(redirect_pos):
                next_redirect_pos = add(redirect_pos, redirect_dir)

                # Rotate until not facing obstacle.
                while is_in_map(next_redirect_pos) and (at(next_redirect_pos) == '#' or next_redirect_pos == obstacle_pos):
                    redirect_dir = rotate_dir(redirect_dir)
                    next_redirect_pos = add(redirect_pos, redirect_dir)

                new_footprint = get_footprint(redirect_pos, redirect_dir)

                # Enter loop.
                if new_footprint in redirect_footprints:
                    possible_obstructions += 1
                    update(obstacle_pos, 'O')
                    break

                redirect_footprints.add(new_footprint)
                redirect_pos = next_redirect_pos

        guard_pos = next_pos

    print(''.join([''.join(row) for row in map]))
    print("part one:", len(visited))
    print("part two:", possible_obstructions)

solve()
