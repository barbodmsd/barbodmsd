from add_commit import create_git_commit
from convert_date import convert_date

matrix = [[0 for _ in range(52)] for _ in range(7)]


def add_letter_A(start_col):
    for row in range(7):
        if row == 0:
            matrix[row][start_col + 1] = 1
            matrix[row][start_col + 2] = 1
        elif row == 1 or row == 2:
            matrix[row][start_col] = 1
            matrix[row][start_col + 3] = 1
        elif row == 3:
            matrix[row][start_col] = 1
            matrix[row][start_col + 1] = 1
            matrix[row][start_col + 2] = 1
            matrix[row][start_col + 3] = 1
        else:
            matrix[row][start_col] = 1
            matrix[row][start_col + 3] = 1


def add_letter_L(start_col):
    for row in range(7):
        if row < 6:
            matrix[row][start_col] = 1
        else:
            matrix[row][start_col] = 1
            matrix[row][start_col + 1] = 1
            matrix[row][start_col + 2] = 1
            matrix[row][start_col + 3] = 1


def add_letter_I(start_col):
    for row in range(7):
        if row == 0 or row == 6:
            matrix[row][start_col + 1] = 1
            matrix[row][start_col] = 1
            matrix[row][start_col + 2] = 1

        matrix[row][start_col + 1] = 1


def add_letter_B(start_col):
    for row in range(7):
        if row == 0 or row == 3 or row == 6:
            matrix[row][start_col] = 1
            matrix[row][start_col + 1] = 1
            matrix[row][start_col + 2] = 1
        else:
            matrix[row][start_col] = 1
            matrix[row][start_col + 3] = 1


def add_letter_J(start_col):
    for row in range(7):
        if row == 0:
            matrix[row][start_col] = 1
            matrix[row][start_col + 1] = 1
            matrix[row][start_col + 2] = 1
        elif row < 6:
            matrix[row][start_col + 1] = 1
        else:
            matrix[row][start_col] = 1


def add_letter_M(start_col):
    for row in range(7):
        matrix[row][start_col] = 1
        matrix[row][start_col + 4] = 1
        if row == 2 or row == 3 or row == 4:
            matrix[row][start_col+row-1] = 1


def add_letter_N(start_col):
    for row in range(7):
        matrix[row][start_col] = 1
        matrix[row][start_col + 4] = 1
        if row == 2 or row == 3 or row == 4:
            matrix[row][start_col+row-1] = 1


def add_letter_D(start_col):
    for row in range(7):
        if row == 0 or row == 6:
            matrix[row][start_col] = 1
            matrix[row][start_col + 1] = 1
            matrix[row][start_col + 2] = 1
        else:
            matrix[row][start_col] = 1
            matrix[row][start_col + 3] = 1


def add_letter_R(start_col):
    """
    Draws the letter 'R' in the matrix starting at start_col.
    """
    for row in range(7):
        if row == 0 or row == 3:
            matrix[row][start_col] = 1
            matrix[row][start_col + 1] = 1
            matrix[row][start_col + 2] = 1
        elif row < 3:
            matrix[row][start_col] = 1
            matrix[row][start_col + 2] = 1
        else:
            matrix[row][start_col] = 1
            matrix[row][start_col + row - 3] = 1


def add_letter_O(start_col):
    """
    Draws the letter 'O' in the matrix starting at start_col.
    """
    for row in range(7):
        if row == 0 or row == 6:
            matrix[row][start_col + 1] = 1
            matrix[row][start_col + 2] = 1
        else:
            matrix[row][start_col] = 1
            matrix[row][start_col + 3] = 1


def add_letter_S(start_col):
    """
    Draws the letter 'S' in the matrix starting at start_col.
    """
    for row in range(7):
        if row == 0 or row == 3 or row == 6:
            matrix[row][start_col] = 1
            matrix[row][start_col + 1] = 1
            matrix[row][start_col + 2] = 1
        elif row < 3:
            matrix[row][start_col] = 1
        else:
            matrix[row][start_col + 2] = 1


def add_letter_M(start_col):
    """
    Draws the letter 'M' in the matrix starting at start_col.
    """
    for row in range(7):
        matrix[row][start_col] = 1  # Left vertical line
        matrix[row][start_col + 4] = 1  # Right vertical line
        if row == 1:
            matrix[row][start_col + row] = 1
            matrix[row][start_col + row+2] = 1
        if row == 2:
            matrix[row][start_col + row] = 1


def add_letter_dash(start_col):
    """
    Draws the letter 'S' in the matrix starting at start_col.
    """
    matrix[3][start_col] = 1
    matrix[3][start_col + 1] = 1
    matrix[3][start_col + 2] = 1
    matrix[3][start_col + 3] = 1


shift = 1
add_letter_B(0+shift)
add_letter_A(5+shift)
add_letter_R(10+shift)
add_letter_B(15+shift)
add_letter_O(20+shift)
add_letter_D(25+shift)
add_letter_dash(31)
add_letter_M(35+shift)
add_letter_S(41+shift)
add_letter_D(46+shift)

# add_letter_A(0+shift)
# add_letter_L(5+shift)
# add_letter_I(10+shift)
# add_letter_B(15+shift)
# add_letter_I(20+shift)
# add_letter_J(24+shift)
# add_letter_A(28+shift)
# add_letter_N(33+shift)
# add_letter_D(39+shift)
# add_letter_I(44+shift)

l = []
# l = [0, 0]

for i in range(52):
    for r in matrix:
        l.append(r[i])


for i in range(len(l)):
    if l[i] == 1:
        for _ in range(5):
            create_git_commit(f"Add name to git for fun",
                              convert_date(2023, i+1), "commit.bin")

# for row in matrix:
#     print("".join(["#" if cell == 1 else " " for cell in row]))
