def bondify(x):
    split = x.split(" ")
    # splits name into first and last name
    name = split[1] + ", " + x
    print (name)

bondify('James Bond')
