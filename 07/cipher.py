import math

def encode_letter(c,r):
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
    return ans[:-1]

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


def make_freq_list(f):
    f = open(f).read()
    words = f.split()
    freq = []
    for i in range(0,26):
        freq.append(0)
    total_letters = 0
    for word in words:
        for letter in word:
            place = ord(letter.lower())
            if place < 123 and place > 96:
                total_letters += 1
                freq[place-97] += 1
    for i in range(0,26):
        freq[i] = freq[i] / float(total_letters)
    return freq

stats = make_freq_list('Sherlock.txt')

def decode(s):
    l = full_encode(s).split('\n')
    curr_dist = distance(stats,build_frequency_vector(l[0]))
    r = l[0]
    for ciph in l[1:]:
        new_dist = distance(stats,build_frequency_vector(ciph))
        #print (ciph)
        if new_dist < curr_dist:
            curr_dist = new_dist
            r = ciph
    return r

s = "The mitochondria is the powerhouse of the cell"
print('The string we will be encoding is: \n' + s)
print('')
rotation = -259234
ciphed = encode_string(s,rotation)
print('Applying a cipher of ' + str(rotation) + ' to the string returns: \n' + ciphed)
print('')
print('Feeding the ciphed string into the decode function returns: \n' + decode(ciphed))


################################
################################
################################
