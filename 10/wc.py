def remove_nonalpha(w):
    result=""
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
    print(f)
    l=[]
    for w in f.split():
        w = w.lower()
        w = remove_nonalpha(w)
        l.append(w)
    d = freq(l)
    return d


d = word_freq("hamlet.txt")
print(d)
