import math

def encode_letter(c,r):
    if r < 0:
        r = 26 + r
    if r > 26:
        r = r % 26
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

print (encode_letter('t', 48))

#print("encode_letter('A',25)" + ' = ' + encode_letter('A',25))
#print("encode_letter('a',-2)" + ' = ' + encode_letter('a',-2))
#print("encode_letter('z',4)" + ' = ' + encode_letter('z',4))
#print("encode_letter('r',7)" + ' = ' + encode_letter('r',7))
#print("")
#print("")

def encode_string(s,r):
    ans = ''
    for i in s:
        if i.isalpha():
            ans += encode_letter(i,r)
        else:
            ans += i
    return ans

#print("encode_string('jordan',7)" + ' = ' + encode_string('jordan',7))
#print("encode_string('b?o?b',3)" + ' = ' + encode_string('b?o?b',3))
#print("encode_string('dog?!?!?!?',5)" + ' = ' + encode_string('dog?!?!?!?',5))
#print("")
#print("")


def full_encode(s):
    ans = ''
    for i in range(0, 26):
        ans += encode_string(s,i) + "\n"
    return ans[:-2]

#print("Printing all possible shifts for 'jordan':")
#print(full_encode('jordan'))


def distance(l1,l2):
    '''
    If the list of are different lengths go to the
    of the shorter one
    '''
    if len(l1)<len(l2):
        length = len(l1)
    else:
        length = len(l2)
    sum = 0
    for i in range(length):
        sum += (l1[i] - l2[i])*(l1[i]-l2[i])
    d = math.sqrt(sum)
    return d

def build_frequency_vector(s):
    s = s.lower()
    spaces = s.count(' ')
    num_letters = float(len(s) - spaces)
    v = []
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        v.append(s.count(letter)/num_letters)
    return v

stats = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]

d = build_frequency_vector('The mitochondria is the powerhouse of he cell')

def decode(s):
    l = full_encode(s).split('\n')
    curr_dist = distance(stats,build_frequency_vector(l[0]))
    r = l[0]
    for ciph in l[1:]:
        new_dist = distance(stats,build_frequency_vector(ciph))
        if new_dist < curr_dist:
            curr_dist = new_dist
            r = ciph
    return r

s = "The mitochondria is the powerhouse of the cell"
print('The string we will be encoding is: \n' + s)
print('')
rotation = 48
ciphed = encode_string(s,rotation)
print('Applying a cipher of ' + str(rotation) + ' to the string returns: \n' + ciphed)
print('')
print('Feeding the ciphed string into the decode function returns: \n' + decode(ciphed))
