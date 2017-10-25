def divide(A,B,u):
    amount = float(A)/B
    # amounts = units received by each person
    ppl = u/amount
    # ppl = number of ppl represented as float
    # converting float to int rounds down to nearest integer
    return int(ppl)

print(divide(5,10,1))
print(divide(1,3,2))
print(divide(5,3,2))
print(divide(0,0,4))
