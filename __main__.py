import itertools

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
        for index in i[1:]:
            if p+index < 0 or p+index >= len(keyboard[pos]): continue
            typos.append(keyboard[pos][p + index])

    # appends the letter itself to typo list
    typos.append(letter)

    return typos

def word_possibilities(word):
    word = list(word)
    wordLength = len(word)
    typoList = [possible_typos(c) for c in word]

    letterPermutations = list(itertools.product(*typoList))
    # joins together chars in nested lists, credits to @orifuwu
    letterPermutations = [''.join(l) for l in letterPermutations]

    return letterPermutations

def main():
    word = input("Word to spellcheck: ")

    # all possible permutations of letters
    permutationsList = word_possibilities(word)

    with open("words.txt") as dictionary_file:
        english_words = dictionary_file.read().split()
        # list holds all possible words that the typo could actually be
        wordList = []
        for i in range(0, len(permutationsList)):
            if permutationsList[i] in english_words:
                wordList.append(permutationsList[i])
        print(wordList)

if __name__ == '__main__':
    main()
