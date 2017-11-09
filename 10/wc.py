def remove_nonalpha(w):
    result=''
    for l in w:
        if l.isalpha():
            result = result + l
    return result

def freq(wordlist):
    d={}
    for w in wordlist:
        d.setdefault(w,0)
        d[w] += 1
    return d

def word_freq(f):
    f = open(f).read()
    l=[]
    for w in f.split():
        w = w.lower()
        w = remove_nonalpha(w)
        l.append(w)
    d = freq(l)
    return d

def word_dict(f):
    f = open(f).read()
    words = [remove_nonalpha(w) for w in f.split()]
    d = {}
    print (words)
    for i in range(0,len(words)-1):
        w = words[i]
        wnext = words[i+1]
        if w in d:
            d[w].append(wnext)
        else:
            d[w] = [wnext]
    last = words[len(words)-1]
    if last not in d:
        d[last] = []
    return d

print word_dict('hamlet.txt')
