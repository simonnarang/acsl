# Simon's ACSL Contest No.3 response 2019—enjoy!
# Kindly please only run with Python3

###################################################
# OTHER METHODS ###################################
###################################################

# Left to right

def add_block_a():
    global current_cell; initial_cell = current_cell
    global blocked_cells
    global sequence
    global last_cell
    global row_size

    for i in range(3): # Move over 3 blocks
        if ((current_cell + 1) not in blocked_cells):
            current_cell += 1
    # Did it work?
    if (current_cell == initial_cell + 3) and not (current_cell > last_cell) and not ((current_cell - 1) % row_size == 0):
        sequence += 'A'
    else: current_cell = initial_cell

def add_block_b():
    global current_cell; initial_cell = current_cell
    global blocked_cells
    global sequence
    global row_size
    if (current_cell + 1) not in blocked_cells: # Move over 1
        current_cell += 1
    if (current_cell + row_size) not in blocked_cells:
        current_cell += row_size # Move down 1 block
    if (current_cell + 1) not in blocked_cells: # Move over 1
        current_cell += 1
    # Did it work?
    if current_cell == initial_cell + 1 + row_size + 1 and not (current_cell > last_cell):
        sequence += 'B'
    else: current_cell = initial_cell

def add_block_c():
    global current_cell; initial_cell = current_cell
    global blocked_cells
    global sequence
    global row_size

    if (current_cell + 1) not in blocked_cells: # Move over 1
        current_cell += 1
    if (current_cell + 1) not in blocked_cells: # Move over 1
        current_cell += 1
    if (current_cell + row_size) not in blocked_cells:
        current_cell += row_size # Move down 1 block
    if (current_cell + row_size) not in blocked_cells:
        current_cell += row_size # Move down 1 block

    # Did it work?
    if current_cell == initial_cell + 1 + 1 + (2 * row_size) and not (current_cell > last_cell):
        sequence += 'C'
    else: current_cell = initial_cell

# Right to left

def sub_block_a():
    global current_cell; initial_cell = current_cell
    global blocked_cells
    global sequence
    global last_cell
    global row_size

    for i in range(3): # Move over 3 blocks
        if ((current_cell - 1) not in blocked_cells):
            current_cell -= 1
    # Did it work?
    if (current_cell == initial_cell - 3) and not (current_cell < 0) and not ((current_cell) % row_size == 0):
        sequence += 'A'
    else: current_cell = initial_cell

def sub_block_b():
    global current_cell
    initial_cell = current_cell
    global blocked_cells
    global sequence
    global row_size
    if (current_cell - 1) not in blocked_cells:  # Move back 1
        current_cell -= 1
    if (current_cell - 1) not in blocked_cells:  # Move back 1
        current_cell -= 1
    if (current_cell - row_size) not in blocked_cells:
        current_cell -= row_size  # Move up 1 block
    # Did it work?
    if current_cell == initial_cell - 2 - row_size and not (current_cell < 0):
        sequence += 'B'
    else:
        current_cell = initial_cell

def sub_block_c():
    global current_cell;
    initial_cell = current_cell
    global blocked_cells
    global sequence
    global row_size

    if (current_cell - 1) not in blocked_cells:  # Move back 1
        current_cell -= 1
    if (current_cell - row_size) not in blocked_cells:
        current_cell -= row_size  # Move up 1 block
    if (current_cell - row_size) not in blocked_cells:
        current_cell -= row_size  # Move up 1 block
    if (current_cell - 1) not in blocked_cells:  # Move back 1
        current_cell -= 1


    # Did it work?
    if current_cell == initial_cell - 2 - (2 * row_size) and not (current_cell < 0):
        sequence += 'C'
    else:
        current_cell = initial_cell

###################################################
# MAIN FUNCTION ###################################
###################################################

def solve(inp):
    global grid; grid = list(map(int, inp.split(' ')))
    column_size = grid[0]
    global row_size; row_size = grid[1]
    global last_cell; last_cell = row_size * column_size
    starting_cell = grid[2]
    global current_cell # Subtract 1 because adding blocks is otherwise additive
    global blocked_cells; blocked_cells = grid[(-1 * grid[3]):]
    direction = starting_cell % row_size == 0 # 0 is left to right; 1 is right to left

    global sequence; sequence = ''
    if not direction:
        # Left to right
        current_cell = starting_cell - 1
        while current_cell == 0 or (current_cell + 1) % row_size != 0:
            add_block_a()
            if current_cell % row_size == 0: break
            add_block_b()
            if current_cell % row_size == 0: break
            add_block_c()
            if current_cell % row_size == 0: break
        print(sequence)
    else:
        # Right to left
        current_cell = starting_cell + 1
        while current_cell != 0 or (current_cell - 1) % row_size != 1:
            sub_block_a()
            if current_cell % row_size == 1: break
            sub_block_b()
            if current_cell % row_size == 1: break
            sub_block_c()
            if current_cell % row_size == 1: break
        print(sequence[::-1])

# The script
with open('input.txt') as f:
    for cov_mat in f:
        cov_mat = cov_mat.rstrip()
        solve(cov_mat)