from heapq import heappop, heappush


def solve():
    grid = []
    start_state = None
    end = None

    # Build grid.
    with open("../input/16.in", "r", encoding='utf-8') as input_file:
        row_idx = 0
        for line in input_file:
            grid.append(line[:-1])

            if start_state is None:
                col_idx = line.find("S")
                if col_idx != -1:
                    # position, direction
                    start_state = ((row_idx, col_idx), (0, 1))

            if end is None:
                col_idx = line.find("E")
                if col_idx != -1:
                    end = (row_idx, col_idx)

            row_idx += 1

    # Priority Queue.
    heap = []

    found = {
        start_state: 0  # state: min-score
        # We should maintain a list of predecessors which have the same "path score".
        # We can then traverse backwards from the destination node and maintain a set of nodes along the best path.
    }

    predecessors = {
        start_state: set()
    }

    heappush(heap, (0, start_state))

    while len(heap) > 0:
        (score, curr_state) = heappop(heap)

        def rotate_left(dir):
            return (dir[1], -dir[0])

        def rotate_right(dir):
            return (-dir[1], dir[0])

        def add(a, b):
            return (a[0] + b[0], a[1] + b[1])

        def at(pos):
            return grid[pos[0]][pos[1]]

        (curr_position, curr_direction) = curr_state

        if curr_position == end:
            print("part 1:", score)
            break

        # Queue valid neighbors.
        neighbors = [(score + 1000, (curr_position, rotate_left(curr_direction))),
                     (score + 1, (add(curr_position, curr_direction), curr_direction)),
                     (score + 1000, (curr_position, rotate_right(curr_direction)))
                     ]

        for neighbor in neighbors:
            (neighbor_score, neighbor_state) = neighbor
            neighbor_pos = neighbor_state[0]

            # Skip neighbor if lower score has already been found.
            if at(neighbor_pos) == '#' or (neighbor_state in found and found[neighbor_state] < neighbor_score):
                continue

            if neighbor_state not in predecessors or found[neighbor_state] > neighbor_score:
                predecessors[neighbor_state] = set()

            predecessors[neighbor_state].add(curr_state)

            found[neighbor_state] = neighbor_score
            heappush(heap, (neighbor_score, neighbor_state))

    # Traverse backwards from destination to find all lowest score paths -> track unique set of tiles along path.
    queue = [(end, dir) for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    best_path_tiles = set()

    while len(queue) > 0:
        curr_state = queue.pop()
        curr_pos = curr_state[0]
        best_path_tiles.add(curr_pos)

        if curr_state in predecessors:
            for predecessor in predecessors[curr_state]:
                queue.append(predecessor)

    for tile in best_path_tiles:
        grid[tile[0]] = grid[tile[0]][:tile[1]] + \
            '0' + grid[tile[0]][tile[1] + 1:]

    print('\n'.join(grid))
    print("part 2:", len(best_path_tiles))


solve()
