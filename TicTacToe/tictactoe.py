clearConsole = lambda: print('\n' * 150)


class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


def makeDictWithCoordsOfChoices(ma):
    choice_position = {}
    chidx = 1
    for i in range(len(ma) - 1, -1, -1):
        for j in range(len(ma[0])):
            choice_position[chidx] = (i, j)
            chidx += 1
    return choice_position


def print_board(ma):
    for i in range(3):
        print('|', end='')
        for j in range(3):
            print(f' {ma[i][j]} |', end='')
        print()
    print()


def valid(ma, i, j):
    if i < 0 or i >= len(ma) or j < 0 or j >= len(ma[0]):
        return False
    return True


def tryWinner(ma, i, j, current_p):
    s = current_p.sign
    if valid(ma, i - 1, j) and valid(ma, i + 1, j) and \
            ma[i - 1][j] == s and ma[i + 1][j] == s:  # up1 down 1
        return current_p
    if valid(ma, i, j - 1) and valid(ma, i, j + 1) and \
            ma[i][j - 1] == s and ma[i][j + 1] == s:  # left1 right1
        return current_p
    if valid(ma, i - 1, j - 1) and valid(ma, i + 1, j + 1) and \
            ma[i - 1][j - 1] == s and ma[i + 1][j + 1] == s:  # leftup1 rightdown1
        return current_p
    if valid(ma, i + 1, j - 1) and valid(ma, i - 1, j + 1) and \
            ma[i + 1][j - 1] == s and ma[i - 1][j + 1] == s:  # leftdown1 rightup1
        return current_p
    # -------------------straights-----------------------------
    if valid(ma, i, j - 2) and ma[i][j - 1] == s and ma[i][j - 2] == s:  # left
        return current_p
    if valid(ma, i, j + 2) and ma[i][j + 1] == s and ma[i][j + 2] == s:  # right
        return current_p
    if valid(ma, i - 2, j) and ma[i - 1][j] == s and ma[i - 2][j] == s:  # up
        return current_p
    if valid(ma, i + 2, j) and ma[i + 1][j] == s and ma[i + 2][j] == s:  # down
        return current_p

    # -------------------diagonals-----------------------------
    if valid(ma, i - 2, j - 2) and ma[i - 1][j - 1] == s and ma[i - 2][j - 2] == s:  # leftup
        return current_p
    if valid(ma, i - 2, j + 2) and ma[i - 1][j + 1] == s and ma[i - 2][j + 2] == s:  # rightup
        return current_p
    if valid(ma, i + 2, j - 2) and ma[i + 1][j - 1] == s and ma[i + 2][j - 2] == s:  # leftdown
        return current_p
    if valid(ma, i + 2, j + 2) and ma[i + 1][j + 1] == s and ma[i + 2][j + 2] == s:  # rightdown
        return current_p


player1_name = input("Player one name: ")
player2_name = input("Player two name: ")

player1_sign = input(f"{player1_name} choose sign 'X' or 'O': ").upper()
while player1_sign not in ['X', 'O']:  # handling wrong input
    player1_sign = input(f"{player1_name} choose sign 'X' or 'O': ").upper()
player2_sign = 'X' if player1_sign == 'O' else 'O'
p1, p2 = Player(player1_name, player1_sign), Player(player2_name, player2_sign)

print(f"This is the numeration of the board:")
print("| 7 | 8 | 9 |")
print("| 4 | 5 | 6 |")
print("| 1 | 2 | 3 |")
print(f"\n{p1.name} is first!\n")

ma = [[' '] * 3 for _ in range(3)]
choice_position = makeDictWithCoordsOfChoices(ma)
winner = None
current_p = p1
starting_player = p1

while not winner:

    i = 1
    while i <= 9:

        choice = int(input((f"{current_p.name} choose a free position [1-9]: ")))
        indx1, indx2 = choice_position[choice][0], choice_position[choice][1]

        if ma[indx1][indx2] == ' ':
            ma[indx1][indx2] = current_p.sign
        else:
            continue
        print_board(ma)

        winner = tryWinner(ma, indx1, indx2, current_p)
        if winner:
            print(f"\n{winner.name} is winner with sign {winner.sign} ")
            exit()

        current_p = p2 if current_p == p1 else p1

        i += 1

    ma = [[' '] * 3 for _ in range(3)]
    clearConsole()
    current_p = p2 if starting_player == p1 else p1
    print(f"No winner this round.\n{current_p.name} first now")
