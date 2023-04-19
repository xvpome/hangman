symbols = ["+","-","*","/"]
def add(n1,n2):
    return n1+n2
def sub(n1, n2):
    return n1-n2
def divide(n1, n2):
    return n1/n2
def times(n1,n2):
    return n1*n2

def calculator():
    first = int(input("What is the first number?: "))
    for x in symbols:
        print(x)
    while True:
        operation = input("Pick an operation: ")
        second = int(input("What is the second number: "))
        result = 0
        if operation == "+":
            result = add(first, second)
        elif operation == "-":
            result = sub(first, second)
        elif operation == "*":
            result = times(first, second)
        elif operation == "/":
            result = divide(first, second)
        print(f"{first} {operation} {second} = {result}")
        choice = input(f"Type 'y' if you wish you continue calculating with {result}. Else, type 'n'\n" )
        first = result
        if choice.lower() == "n":
            break
calculator()
