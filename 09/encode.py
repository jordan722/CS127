def encode(s):
    ans = []
    if len(s)<=1:
        return [s]
    curr = s[0]
    for i in range(1,len(s)):
        if s[i] == curr[0]:
            curr += s[i]
        else:
            if len(curr) > 1:
                ans.append(len(curr))
            ans.append(curr[0])
            curr = s[i]
    if len(curr) > 1:
        ans.append(len(curr))
    ans.append(curr[0])
    return ans

print(encode(''))
print(encode('baa'))
print(encode('zzzzzzzzz'))
print(encode('aaaaaaabbbbe'))
print(encode('aabcccdeeeeaaa'))
