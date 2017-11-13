def remove_nonalpha(w):
    result=''
    for l in w:
        if l.isalpha():
            result = result + l
    return result



print word_dict('hamlet.txt')
