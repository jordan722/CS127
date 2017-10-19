def check(game):
    n = len(game)
    if game[0] != '_' and game[0] != game[i+1]:
        return False
    for i in range(1,n-1):
        if game[i] != '_' and game[i] != game[i-1] and game[i] != game[i+1]:
            return False
    if game[n] != '_' and game[n] != game[n-1]:
        return False
    return True

def ladybug(inp):
    lines = inp.split('\n')
    games = []
    for i in range(1,len(lines),2):
        games.append([ x for x in lines[i+1]])
    for game in games:
        print("Game is here")
        print(game)
        print(check_game(game))

def check_game(game):
    if game.count('_') == 0:
        if check(game):
            return "YES"
        else:
            return "NO"
    checked = ['_']
    for i in game:
        if i not in checked:
            if game.count(i) == 1:
                return "NO"
            checked.append(i)
    return "YES"



inp = "4\n7\nRBY_YBR\n6\nX_Y__X\n2\n__\n6\nB_RRBR"
ladybug(inp)
