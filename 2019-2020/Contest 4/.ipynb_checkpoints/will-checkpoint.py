# Will Wang - 12th Grade
# Pittsford Sutherland High School
# American Computer Science League - Intermediate Division
# Contest 3
# PYTHON 4

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
squares = [9, 16, 25, 36, 49]

row_col_change = [6, 11, 16, 21, 26, 34, 39, 44, 49]


def check_move(positions, pos, roll):
    for i in range(len(positions)):
        if pos + roll == positions[i] or pos + roll > 52:
            return False
    return True


def solve(inp_array):
    cpu_positions = list(map(int, inp_array[:3]))
    player_positions = list(map(int, inp_array[3:6]))
    move_array = list(map(int, inp_array[7:]))
    for i in range(len(move_array)):

        roll = move_array[i]
        cpu_positions = sorted(cpu_positions)
        player_positions = sorted(player_positions)
        occupied_positions = cpu_positions + player_positions
        # print("Round ", i, occupied_positions, " Roll ", roll)
        if check_move(occupied_positions, player_positions[0], roll):
            player_positions[0] += roll
            if player_positions[0] == 52:
                player_positions[0] = 99
            elif player_positions[0] in primes:
                # print("PRIME")
                occupied_positions = cpu_positions + player_positions
                for p in range(6):
                    if player_positions[0] + 1 not in occupied_positions:
                        player_positions[0] += 1
                        occupied_positions = cpu_positions + player_positions
                    else:
                        break
            elif player_positions[0] in squares:
                # print("SQUARES")
                occupied_positions = cpu_positions + player_positions
                for j in range(6):
                    if player_positions[0] - 1 not in occupied_positions:
                        player_positions[0] -= 1
                        occupied_positions = cpu_positions + player_positions
                    else:
                        break
            else:

                valid_positions = []
                change = False
                for n in range(roll + 1):
                    if player_positions[0] - roll + n in row_col_change and n < roll - 1:
                        # print("ROW CHANGE")
                        change = True
                if change:
                    for m in range(roll + 1):
                        temp_pos = player_positions[0] - roll + m
                        if temp_pos % roll == 0 and temp_pos not in occupied_positions[0:3] + occupied_positions[4:6]:
                            valid_positions.append(temp_pos)
                    if valid_positions:
                        player_positions[0] = max(valid_positions)
                    else:
                        player_positions[0] -= roll
        else:
            player_positions = player_positions
    return sorted(player_positions)


for inp in range(5):
    input_array = input().split(' ')
    ans = solve(input_array)
    print(''.join((str(a) + ' ' for a in ans)))
