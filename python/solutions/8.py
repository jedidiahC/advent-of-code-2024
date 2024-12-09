def diff(pos1, pos2):
    return (pos1[0] - pos2[0], pos1[1] - pos2[1])

def add(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])

def get_antinode_positions(pos1, pos2):
    delta = diff(pos1, pos2)
    return [add(pos1, delta), diff(pos2, delta)]

def get_new_antinode_positions(pos1, pos2, is_within_grid):
    antinodes = []
    delta = diff(pos1, pos2)
    while is_within_grid(pos1):
        antinodes.append(pos1)
        pos1 = add(pos1, delta)
    while is_within_grid(pos2):
        antinodes.append(pos2)
        pos2 = diff(pos2, delta)
    return antinodes

def solve(is_part_two):
    antennas = {}
    map = []

    with open("../input/8.in", "r") as input_file:
        height = 0
        y = 0
        for line in input_file:
            width = len(line) - 1
            x = 0

            map.append([])
            for char in line:
                if char != '.':
                    if char not in antennas:
                        antennas[char] = []
                    antennas[char].append((y, x))
                map[-1].append(char)

                x += 1
            y += 1
            height += 1

        print(height, width)

    def within_grid(pos):
        return pos[0] >= 0 and pos[0] < height and pos[1] >= 0 and pos[1] < width

    antinodes = set()

    for antenna_group in antennas.values():
        # We need at least 2 antennas to get an antinode.
        if len(antenna_group) < 2:
            break

        # Find all unique pairs of matching antennas:
        for a in range(0, len(antenna_group) - 1):
            for b in range(a + 1, len(antenna_group)):
                antenna_pos_1, antenna_pos_2  = antenna_group[a], antenna_group[b]
                if is_part_two:
                    antinode_positions = get_new_antinode_positions(antenna_pos_1, antenna_pos_2, is_within_grid=within_grid)
                else:
                    antinode_positions = get_antinode_positions(antenna_pos_1, antenna_pos_2)

                for antinode_pos in antinode_positions:
                    if within_grid(antinode_pos):
                        antinodes.add(antinode_pos)
                        map[antinode_pos[0]][antinode_pos[1]] = '#'

    print(''.join([''.join(row) for row in map]))
    print(len(antinodes))

solve(False)
solve(True)
