def score(w):
    values = {1:['A','E','I','O','U','L','N','R','S','T'],
    2:['D','G'],
    3:['B','C','M','P'],
    4:['F','H','V',''],
    5:['K'],
    8:['J,X'],
    10:['Q','Z']}
    ans = 0
    for letter in w:
        for key,val in values.items():
            if letter.upper() in val:
                ans += key
    return ans

print(score(''))
print(score('hello'))
print(score('zebra'))
