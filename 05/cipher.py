def encode_letter(c,r):
    if r < 0:
        r = 26 + r
    if c.islower():
        place = ord(c)+ r
        if place < 123:
            return chr(place)
        return (chr(97 + (ord(c)+r)%123))
    if c.isupper():
        place = ord(c)+ r
        if place < 91:
            return chr(place)
        return (chr(65 + (ord(c)+r)%91))

print("encode_letter('A',25)" + ' = ' + encode_letter('A',25))
print("encode_letter('a',-2)" + ' = ' + encode_letter('a',-2))
print("encode_letter('z',4)" + ' = ' + encode_letter('z',4))
print("encode_letter('r',7)" + ' = ' + encode_letter('r',7))
print("")
print("")

def encode_string(s,r):
    ans = ''
    for i in s:
        if i.isalpha():
            ans += encode_letter(i,r)
        else:
            ans += i
    return ans

print("encode_string('jordan',7)" + ' = ' + encode_string('jordan',7))
print("encode_string('b?o?b',3)" + ' = ' + encode_string('b?o?b',3))
print("encode_string('dog?!?!?!?',5)" + ' = ' + encode_string('dog?!?!?!?',5))
print("")
print("")


def full_encode(s):
    ans = ''
    for i in range(0, 26):
        ans += encode_string(s,i) + "\n"
    return ans

print("Printing all possible shifts for 'jordan':")
print(full_encode('jordan'))
