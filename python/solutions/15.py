from typing import Tuple


def get_level():
    warehouse = []
    moves = []
    lantern_fish = None
    with open("../input/15.in", "r", encoding='utf-8') as input_file:
        reading_map = True
        for line in input_file:
            if line == '\n':
                reading_map = False
                continue

            if reading_map:
                x_pos = line.find('@')
                if x_pos != -1:
                    lantern_fish = (len(warehouse), x_pos)
                warehouse.append([c for c in line][:-1])
                continue

            for c in line:
                if c == "<":
                    moves.append((0, -1))
                elif c == '^':
                    moves.append((-1, 0))
                elif c == '>':
                    moves.append((0, 1))
                elif c == 'v':
                    moves.append((1, 0))

    return warehouse, moves, lantern_fish


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def at(pos, warehouse):
    return warehouse[pos[0]][pos[1]]


def swap(a, b, warehouse):
    warehouse[a[0]][a[1]], warehouse[b[0]][b[1]] = at(
        b, warehouse), at(a, warehouse)


def print_warehouse(warehouse):
    print("---")
    print('\n'.join([''.join(row) for row in warehouse]))
    print("---")


def solve_part_one():
    (warehouse, moves, lantern_fish) = get_level()

    for move in moves:
        next_pos = add(lantern_fish, move)

        if at(next_pos, warehouse) == '#':
            continue

        if at(next_pos, warehouse) == '.':
            swap(lantern_fish, next_pos, warehouse)
            lantern_fish = next_pos
            continue

        # Attempt move.
        box_pos = next_pos
        while at(box_pos, warehouse) != '.' and at(box_pos, warehouse) != '#':
            box_pos = add(box_pos, move)

        # Immovable.
        if at(box_pos, warehouse) == '#':
            continue

        # Move boxes.
        reverse_move = (-1 * move[0], -1 * move[1])
        while at(box_pos, warehouse) == '.':
            swap(box_pos, add(box_pos, reverse_move), warehouse)
            if at(box_pos, warehouse) == '@':
                break
            box_pos = add(box_pos, reverse_move)

        lantern_fish = next_pos

    print_warehouse(warehouse)

    result = 0
    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if at((y, x), warehouse) == 'O':
                gps_coordinate = y * 100 + x
                result += gps_coordinate

    print(result)


def upgrade_level(level):
    (warehouse, moves, lantern_fish) = level
    new_warehouse = []
    for warehouse_row in warehouse:
        row = []
        for tile in warehouse_row:
            if tile == '#':
                row.extend(['#', '#'])
            elif tile == 'O':
                row.extend(['[', ']'])
            elif tile == '.':
                row.extend(['.', '.'])
            else:
                row.extend(['@', '.'])
        new_warehouse.append(row)
    return (new_warehouse, moves, (lantern_fish[0], lantern_fish[1] * 2))


def can_push(current_pos: Tuple, push_dir: Tuple, warehouse) -> bool:
    '''
    box_pos refers to the coordinate of the "[" part of the box.
    '''

    at_current_pos = at(current_pos, warehouse)

    if at_current_pos == '#':
        return False

    if at_current_pos == '.':
        return True

    box_left_pos = current_pos if at_current_pos == '[' else add(
        current_pos, (0, -1))

    box_right_pos = add(box_left_pos, (0, 1))

    target_pos_left = add(box_left_pos, push_dir)
    target_pos_right = add(box_right_pos, push_dir)

    at_target_left = at(target_pos_left, warehouse)
    at_target_right = at(target_pos_right, warehouse)

    # Vertical push.
    if push_dir[0] != 0:
        if at_target_left == '[' and at_target_right == ']':
            return can_push(target_pos_left, push_dir, warehouse)

        return can_push(target_pos_left, push_dir, warehouse) and can_push(target_pos_right, push_dir, warehouse)

    # Left push.
    if push_dir[1] == -1:
        return can_push(target_pos_left, push_dir, warehouse)

    # Right push.
    return can_push(target_pos_right, push_dir, warehouse)


def push(current_pos: Tuple, push_dir: Tuple, warehouse) -> bool:
    '''
    box_pos refers to the coordinate of the "[" part of the box.
    '''

    at_current_pos = at(current_pos, warehouse)

    if at_current_pos != '[' and at_current_pos != ']':
        return

    box_left_pos = current_pos if at_current_pos == '[' else add(
        current_pos, (0, -1))

    box_right_pos = add(box_left_pos, (0, 1))

    target_pos_left = add(box_left_pos, push_dir)
    target_pos_right = add(box_right_pos, push_dir)

    at_target_left = at(target_pos_left, warehouse)
    at_target_right = at(target_pos_right, warehouse)

    # Vertical push.
    if push_dir[0] != 0:
        # Box to push perfectly aligned
        if at_target_left == '[' and at_target_right == ']':
            push(target_pos_left, push_dir, warehouse)
        else:
            push(target_pos_left, push_dir, warehouse)
            push(target_pos_right, push_dir, warehouse)

        # Move box into new place.
        swap(target_pos_left, box_left_pos, warehouse)
        swap(target_pos_right, box_right_pos, warehouse)

    # Push left.
    if push_dir[1] == -1:
        push(target_pos_left, push_dir, warehouse)
        swap(target_pos_left, box_left_pos, warehouse)
        swap(box_left_pos, box_right_pos, warehouse)
    elif push_dir[1] == 1:
        # Push right:
        push(target_pos_right, push_dir, warehouse)
        swap(target_pos_right, box_right_pos, warehouse)
        swap(box_left_pos, box_right_pos, warehouse)


def solve_part_two():
    (warehouse, moves, lantern_fish) = upgrade_level(get_level())

    for move in moves:
        print_warehouse(warehouse)
        next_pos = add(lantern_fish, move)

        # Blocked.
        if at(next_pos, warehouse) == '#':
            continue

        # Normal move.
        if at(next_pos, warehouse) == '.':
            swap(lantern_fish, next_pos, warehouse)
            lantern_fish = next_pos
            continue

        # Try move box.
        if can_push(next_pos, move, warehouse):
            push(next_pos, move, warehouse)
            swap(lantern_fish, next_pos, warehouse)
            lantern_fish = next_pos

    result = 0
    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if at((y, x), warehouse) == '[':
                gps_coordinate = y * 100 + x
                result += gps_coordinate

    print(result)


# solve_part_one()
solve_part_two()
