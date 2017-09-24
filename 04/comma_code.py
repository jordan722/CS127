def comma_code(l):
    size = len(l)
    if size == 0:
        return "Empty string"
    if size == 1:
        return l[0]
    if size == 2:
        return l[0] + ' and ' + l[1]
    ans = ''
    for i in range(0,size-1):
        ans += l[i] + ', '
    return ans + 'and ' + l[-1]

spam = ['apples','bananas','tofu','cats']
test = ['apples']
test2 = ['apples','bananas']
test3 = []
print(str(spam) + ' = ' + comma_code(spam))
print(str(test) + ' = ' + comma_code(test))
print(str(test2) + ' = ' + comma_code(test2))
print(str(test3) + ' = ' + comma_code(test3))
