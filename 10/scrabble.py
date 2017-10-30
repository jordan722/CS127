TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10), (7,7))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

def make_scrabble_board():
    board=[]
    for i in range(15):
        line=[]
        for i in range(15):
            line.append('_')
        board.append(line)

    for r,c in TRIPLE_WORD_SCORE:
        board[r][c] = 'T'

    for r,c in DOUBLE_WORD_SCORE:
        board[r][c] = 'D'

    for r,c in TRIPLE_LETTER_SCORE:
        board[r][c]='t'

    for r,c in DOUBLE_LETTER_SCORE:
        board[r][c] = 'd'
    return board

def score(w,b):
    print(b)
    values = {1:['A','E','I','O','U','L','N','R','S','T'],
    2:['D','G'],
    3:['B','C','M','P'],
    4:['F','H','V','W','Y'],
    5:['K'],
    8:['J','X'],
    10:['Q','Z']}
    ans = 0
    for letter,p in zip(w,b):
        for key,val in values.items():
            if letter.upper() in val:
                add = key
                if p == 'd':
                    add *= 2
                if p == 't':
                    add *= 3
                ans += add
    for i in range(0,b.count('D')):
        ans *= 2
    for i in range(0,b.count('T')):
        ans *= 3
    return ans

def add_word_across(board,word,r,c):
    if (c+len(word)) > len(board[r]):
        return 0
    b = board[r][c:c+len(word)]
    return score(word,b)

def add_word_down(board,word,r,c):
    if (r+len(word)) > len(board):
        return 0
    b = []
    for i in range(0,len(word)):
        b.append(board[r+i][c])
    return score(word,b)

def print_board(b):
    for line in b:
        print ( ' '.join(line))

board = make_scrabble_board()
print_board(board)

print(add_word_across(board,'zebra',0,2))
print(add_word_down(board,'zebra',0,2))
