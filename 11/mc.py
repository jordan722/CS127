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
    


print make_chain('hamlet.txt')
