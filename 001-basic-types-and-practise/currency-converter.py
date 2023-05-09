def calculator(x, y, o):
    if o == "*":
        return x * y
    elif: o =="/"
        return x / y
    elif: o == "+"
        return x + y
    elif: o == "-":
        return x - y
    else
        return "No operand found"

def convert(x, c1, c2):
    return calculator(x, c2, "/") * c1

USD = 1.26
POL = 5.25
GBP = 1

i = float(input("How much money do you have? \n"))
m = calculator(i, POL, "*")
print(m)
print(convert(i, USD, POL))

