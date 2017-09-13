def string_times(str, n):
    i = n
    ans = ""
    while i > 0:
        ans += str
        i -= 1
    return ans

print ("string_times('hi',3) = " + string_times('hi',3))


def front_times(str, n):
    if len(str) > 2:
        front = str[:3]
    else:
        front = str
    i = n
    ans = ''
    while i > 0:
        ans += front
        i -= 1
    return ans

print ("front_times('Chocolate', 2) = " + front_times('Chocolate', 2))


def string_bits(str):
    ans = ""
    i = 0
    while i < len(str):
        if i % 2 == 0:
            ans += str[i]
        i += 1
    return ans

print ("string_bits('Heeololeo') = " + string_bits('Heeololeo'))


def lone_sum(a, b, c):
    sum = 0
    if (a != b and a != c):
        sum += a
    if (b != a and b != c):
        sum += b
    if (c != a and c != b):
        sum += c
    return sum

print ("lone_sum(3, 2, 3) = " + str(lone_sum(3, 2, 3)))


def string_splosion(str):
    ans = ""
    i = 1
    while i <= len(str):
        ans += str[:i]
        i += 1
    return ans

print ("string_splosion('fade') = " + string_splosion('fade'))


def cigar_party(cigars, is_weekend):
    if cigars < 40:
        return False
    else:
        if is_weekend:
            return True
        else:
            return cigars <= 60

print ("cigar_party(50, True) = " + str(cigar_party(50, True)))


def caught_speeding(speed, is_birthday):
    lim = 60
    small = 80
    if is_birthday:
        lim += 5
        small += 5
    if speed <= lim:
        return 0
    if speed <= small:
        return 1
    return 2

print ("caught_speeding(65, True) = " + str(caught_speeding(65, True)))
