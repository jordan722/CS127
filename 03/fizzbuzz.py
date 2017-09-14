def fizz_buzz():
    for i in range(1,101):
        ans = str(i)
        if i % 3 == 0:
            ans = 'fizz'
        if i % 5 == 0:
            ans = 'buzz'
        if i % 3 == 0 and i % 5 == 0:
            ans = 'fizz buzz'
        print (ans)

fizz_buzz()
