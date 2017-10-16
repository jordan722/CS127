def fruit(string):
    lines = string.split('\n')
    s, t = lines[0].strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = lines[1].strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = lines[2].strip().split(' ')
    m, n = [int(m), int(n)]
    dapple = [int(x) for x in lines[3].strip().split(' ')]
    dorange = [int(x) for x in lines[4].strip().split(' ')]
    applepos = [a + x for x in dapple]
    orangepos = [b + x for x in dorange]
    print(applepos)
    print(orangepos)
    houseapples = 0
    houseoranges = 0
    for pos in applepos:
        if pos <= t and pos >= s:
            houseapples +=1
    print(houseapples)
    for pos in orangepos:
        if pos <= t and pos >= s:
            houseoranges +=1
    print(houseoranges)


inp = "7 11\n 5 15\n 3 2\n -2 2 1\n 5 -6"

fruit(inp)
