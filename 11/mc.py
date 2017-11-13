import random
def remove_nonalpha(w):
    result=''
    for l in w:
        if l.isalpha():
            result = result + l
    return result

def make_chain(f):
    f = open(f).read()
    l = f.split()
    l = [remove_nonalpha(x) for x in l]
    l = [x.lower() for x in l]
    d = {}
    for i in range(2,len(l)):
        a = l[i-2]
        b = l[i-1]
        d.setdefault((a,b),[])
        d[(a,b)].append(l[i])
    return d

def generate_text(d, start_word, length=50):
    wordlist = []
    l = dict((k,v) for k,v in d.items() if k[1] == start_word)
    curr = start_word
    n = random.choice(random.choice(l.values()))
    print n
    for i in range(length):
        if (curr,n) not in d:
            break
        wordlist.append(n)
        key = (curr,n)
        curr = n
        n = random.choice(d[key])
    return " ".join(wordlist)

print make_chain('hamlet.txt')
print generate_text(make_chain('hamlet.txt'), 'to')
