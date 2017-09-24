def collatz(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


def collatz_input():
    n = raw_input("Enter an integer:\n")
    try:
        n = int(n)
        while True:
            print(n)
            if n == 1:
                return "Completed"
            n = collatz(n)
    except:
        return "Please enter an integer"

print('collatz(4) = ' + str(collatz(4)))
print('collatz(9) = ' + str(collatz(9)))
print('collatz(10) = ' + str(collatz(10)))

print collatz_input()
