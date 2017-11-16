import csv

def remove_nonalpha(w):
    letters = ""
    for l in w:
        if l.isalpha() or l=="'":
            l = l.lower()
            letters += l
    return letters


def make_dict(f):
    info = open(f)
    info = csv.DictReader(info)
    data = []
    for line in info:
        data.append(line)
    dic = {}
    for offender in data:
        num = offender['TDCJ Number']
        s = offender['Last Statement']
        for word in s.split(' '):
            word = remove_nonalpha(word)
            if word in dic:
                if num not in dic[word]:
                    dic[word].append(num)
            else:
                dic[word] = [num]
    return dic


def search_offenders(s):
    words = make_dict('offenders-clean.csv')
    return words[s]


print(make_dict('offenders-clean.csv'))
print()
print("Inmates who stated 'miss' in their final statements: " + str(search_offenders('miss')))
