def freq(n,l):
    total = 0
    for i in l:
        if i == n:
            total += 1
    return total

print(freq(3,[3,2,2,1,3,4,5,4,3,4,3]))

def min(l):
    lowest = l[0]
    for i in l:
        if i < lowest:
            lowest = i
    return lowest

print(min([3,4,5,62,3,23,34,122,3,4,3]))

def mode(l):
    highest = 0
    for i in l:
        curr = freq(i,l)
        if curr > highest:
            highest = i
    return highest

print(mode([3,4,5,62,3,23,23,34,122,23,3,4,23,23,3]))
