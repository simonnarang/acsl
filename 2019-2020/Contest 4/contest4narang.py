class Board:
    sq = [9, 16, 25, 36, 49]
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    pivot = [7, 12, 17, 22, 27, 35, 40, 45, 50]
    def __init__(self, player_starting_locs, opponent_starting_locs):
#         print('Creating board')
        self.markers = []
        for loc in player_starting_locs:
            self.markers.append(Marker(loc, True))
        for loc in opponent_starting_locs:
            self.markers.append(Marker(loc, False))
        self.markers.sort()
#         print(repr(self.markers))
    def move_marker(self, dice_roll, is_incremental):
        if is_incremental: pass #print('Incremental move...')
#         else: print('Moving...')
        current_marker = self.markers[0]
        for m in self.markers:
            if m.get_is_player(): 
                current_marker = m
                break
        # Conditions 4, 5, 6
        for m in self.markers[1:]:
            if m.get_loc() == current_marker.get_loc() + dice_roll or 52 < current_marker.get_loc() + dice_roll:
#                 print('Cannot move marker ' + repr(current_marker) + ' by ' + str(dice_roll)+'. Would overlap with other marker OR be > 52')
                return
        current_marker.set_loc(current_marker.get_loc() + dice_roll)
        if not is_incremental:
            # Condition 7
            if current_marker.get_loc() in self.prime and not is_incremental:
                for i in range(0,6): self.move_marker(1, True)
            # Condition 8
            elif current_marker.get_loc() in self.sq:
                for i in range(0,6): self.move_marker(-1, True)
            # Condition 9
            else:
                pivotted = False
                for loc in range(current_marker.get_loc() - dice_roll, current_marker.get_loc()):
                    if loc in self.pivot and loc - (current_marker.get_loc() - dice_roll) > 1:
                        pivotted = True
                        break
                if pivotted:
#                     print('PIVOTTED going from ' + str(current_marker.get_loc()-dice_roll) + ' to '+ str(current_marker.get_loc()))
                    for loc in range(current_marker.get_loc() - dice_roll + 1, current_marker.get_loc()):
                        if loc % dice_roll == 0:
                            current_marker.set_loc(current_marker.get_loc() - dice_roll)
#                             print(loc - current_marker.get_loc())
                            self.move_marker(loc - (current_marker.get_loc()), True)
            self.markers.sort()
#             print(repr(self.markers))
    def get_player_locs(self):
        for m in self.markers:
            if m.get_is_player(): yield m.get_loc()
                
class Marker:
    def __init__(self, init_loc, is_player):
        self.prior_loc = 0
        self.loc = int(init_loc)
        self.is_player = is_player
#         print('Created new marker at ' + init_loc)
    def get_loc(self):
        return self.loc
    def set_loc(self, new_loc):
        self.loc = new_loc
        return
    def get_is_player(self):
        return self.is_player
    def __repr__(self):
        return str([int(self.is_player), self.loc])
    def __lt__(self, other):
        return self.loc < other.get_loc()
    
input_text = open('input.txt')
for l in input_text:
#     print('Input: ' + l)
    l = l.split(' ')
    opponent_markers = l[0:3]
    player_markers = l[3:6]
    board = Board(player_markers, opponent_markers)
    num_dice = l[6]
    dice_rolls = l[7:7+int(num_dice)]
    for roll in dice_rolls:
        board.move_marker(int(roll), False)
    player_locs = board.get_player_locs()
    output_str = ''
    for p in player_locs:
        output_str += str(p)
        output_str += ' '
    print(output_str)