def piglatinify(str):
    words = str.split(' ')
    vowels = ['a','e','i','o','u']
    ans = ''
    for w in words:
        if not w:
            ans += ' '
            continue
        first = w[0]
        if first in vowels:
            new = w + 'ay'
        else:
            new = w[1:] + first + 'ay'
        ans += new + ' '
    return ans

print (piglatinify('i went to             the store'))
