def rle_encode(l):
    ans = ''
    i = 0
    while i < len(l):
        if type(l[i]) is int:
            for x in range(0,l[i]):
                ans += l[i+1]
            i += 2
        else:
            ans += l[i]
            i += 1
    return ans

l = [2,'a', 3, 'b', 'c', 2,'d']
print(l)
print(rle_encode(l))

l2 = [4,'z', 'b', 'c', 2,'d']
print(l2)
print(rle_encode(l2))

l3 = ['x', 3, 's', 6, 'c', 'd']
print(l3)
print(rle_encode(l3))

l4 = [7,'a', 3, 'b', 'c', 'd']
print(l4)
print(rle_encode(l4))
