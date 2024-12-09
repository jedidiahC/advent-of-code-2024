class Block:
    # file_id is -1 if free block.
    def __init__(self, file_id, size):
        self.file_id = file_id
        self.size = size
        self.next = None
        self.prev = None

    def __str__(self):
        return f'{"free" if self.file_id == -1 else self.file_id}[{self.size}]'

    def print_list(self):
        curr = self
        result = []
        while curr != None:
            result.append(str(curr))
            curr = curr.next
        print(", ".join(result))

    def checksum(self):
        curr = self
        index = 0

        checksum = 0
        while curr != None:
            if curr.file_id != -1:
                checksum += sum(range(index, index + curr.size)) * curr.file_id
            index += curr.size
            curr = curr.next

        return checksum

def build_block_ll():
    head = Block(-1, 0)
    current = head

    with open("../input/9.in", "r") as input_file:
        line = input_file.read().strip()

        for index, char in enumerate(line):
            is_free = index % 2 != 0
            current_file_id = -1 if is_free else int(index / 2)
            block_size = int(char)

            new_block = Block(current_file_id, block_size)
            new_block.prev = current
            current.next = new_block
            current = new_block

    return (head, current)

def solve_part_one():
    (head, tail) = build_block_ll()
    next_free_block = head.next
    end_block = tail

    while next_free_block != end_block:
        # Ensure end pointer always point at a non-free block.
        if end_block.file_id == -1 or end_block.size == 0:
            end_block = end_block.prev
            end_block.next = None
            continue

        # Ensure next free block is actually free.
        if next_free_block.file_id != -1:
            next_free_block = next_free_block.next
            continue

        # Try to allocate as much of the end block to the start.
        if next_free_block.file_id == -1:
            # Remove free block when size 0.
            if next_free_block.size == 0:
                next_free_block.prev.next = next_free_block.next
                next_free_block.next.prev = next_free_block.prev
                next_free_block = next_free_block.next
                continue

            # Shift as much of end_block to next_free_block.
            before_free_block = next_free_block.prev
            moved_block = Block(end_block.file_id, min(next_free_block.size, end_block.size))

            next_free_block.size -= moved_block.size
            end_block.size -= moved_block.size

            before_free_block.next = moved_block
            next_free_block.prev = moved_block
            moved_block.next = next_free_block
            moved_block.prev = before_free_block

    print(head.next.checksum())

def solve_part_two():
    (head, tail) = build_block_ll()
    end_block = tail

    while end_block != head:
        # Ensure end pointer always point at a non-free block.
        if end_block.file_id == -1 or end_block.size == 0:
            end_block = end_block.prev
            continue

        # Try to find the left-most span of free space.
        free_block = None
        curr_block = end_block.prev
        while curr_block != head:
            if curr_block.file_id == -1 and curr_block.size >= end_block.size:
                free_block = curr_block
            curr_block = curr_block.prev

        if free_block == None:
            end_block = end_block.prev
            continue

        moved_block = Block(end_block.file_id, end_block.size)
        moved_block.prev = free_block.prev
        moved_block.prev.next = moved_block
        moved_block.next = free_block

        free_block.prev = moved_block
        free_block.size -= moved_block.size

        end_block.file_id = -1
        end_block = end_block.prev

    print(head.next.checksum())

solve_part_one()
solve_part_two()
