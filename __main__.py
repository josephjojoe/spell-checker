# keyboard layout, can change based on your keyboard
keyboard = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
]

def possible_typos(letter):
    # positions of nearby letters
    # in format (y offset, x offsets)
    # e.g [-1, 0, 1] is y offset -1 (line above)
    #     0 means same position and 1 means to the right
    indexes = [[-1, 0, 1], [0, -1, 1], [1, -1, 0]]

    # find row (line_index) and column (p)
    line_index = 0
    p = 0
    for x, k in enumerate(keyboard):
        if k.find(letter) != -1:
            line_index = x
            p = k.find(letter)

    # go through each possible typo line
    typos = []
    for i in indexes:
        # offset row by current Y
        pos = line_index + i[0]
        # if it's outside the keyboard skip
        if pos < 0 or pos >= len(keyboard): continue
        # go through each X offset and add it to the list
        for index in i[1:]: typos.append(keyboard[pos][p + index])

    return typos
