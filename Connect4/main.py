def printMatrix(ma):
    for row in ma:
        print(row)


_rows_ = 6
_cols_ = 7

ma = [[0] * _cols_ for _ in range(_rows_)]

pidx = 1
player = 1
winner = None


def makinLine(ma, row, col, player, pr, pc):
    for _ in range(3):
        row, col = row + pr, col + pc
        if ma[row][col] != player:
            return False
    return True


def try4matches(ma, row, col, player):
    # todo Walk through the 8 lines of winning condition and check if there are !!FOUR!! {player}'s (ONE's or TWO's)
    if col + 3 < len(ma[0]) and makinLine(ma, row, col, player, 0, 1):
        return player  # right

    if col - 3 >= 0 and makinLine(ma, row, col, player, 0, -1):
        return player  # left

    if row + 3 < len(ma) and makinLine(ma, row, col, player, 1, 0):
        return player  # down

    if row + 3 < len(ma) and col + 3 < len(ma[0]) and makinLine(ma, row, col, player, 1, 1):
        return player  # down right diagonal

    if row + 3 < len(ma) and col - 3 >= 0 and makinLine(ma, row, col, player, 1, -1):
        return player  # down left diagonal

    if row - 3 >= 0 and col + 3 < len(ma[0]) and makinLine(ma, row, col, player, -1, 1):
        return player  # up right diagonal

    if row - 3 >= 0 and col - 3 >= 0 and makinLine(ma, row, col, player, -1, -1):
        return player  # up left diagonal

    return None  # means no winner for now


for turn in range(
        _rows_ * _cols_):  # is max turns wich the game has with this matrix size so if is jumped over means matrix is filled and NO WINNER
    chosen_col = int(input(f"Player {player}, please choose a column\n")) - 1
    if chosen_col < 0 or chosen_col >= _cols_:
        print("Greshka peeras na kolonata")
        continue

    for rowi in range(_rows_ - 1, -1, -1):
        if ma[rowi][chosen_col] == 0:
            ma[rowi][chosen_col] = player
            break

    winner = try4matches(ma, rowi, chosen_col, player)

    printMatrix(ma)

    if winner:
        break

    pidx += 1
    player = 2 if pidx % 2 == 0 else 1

if not winner:
    print(f"GG WP NO WINNER!")
else:
    print(f"Winner is player: !!! {winner} !!!")
