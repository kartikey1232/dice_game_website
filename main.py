import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def exp(n1,n2):
    return n1**n2
while(True):
    result = 0
    n1=float(input("Enter the first number\n"))
    print("+\n-\n*\n/\n^")
    operator=input("Pick a operation\n")
    n2=float(input("What's the next number?\n"))
    if operator == "+":
        result+=add(n1,n2)
        print(f"{n1} + {n2} = {result}")
    elif operator == "-":
        result+=sub(n1,n2)
        print(f"{n1} - {n2} = {result}")
    elif operator == "*":
        result+=mul(n1,n2)
        print(f"{n1} * {n2} = {result}")
    elif operator == "/":
        result+=div(n1,n2)
        print(f"{n1} / {n2} = {result}")
    else :
        result+=exp(n1,n2)
        print(f"{n1} ^ {n2} = {result}")
    while(True):
        choice=input(f"Type 'y' to continue calculating with {result}, or typne 'n' to start a new calculation\n")
        if choice=="y":
            n1=result
            result=0
            operator = input("Pick a operation\n")
            n2 = float(input("What's the next number?\n"))
            if operator == "+":
                result += add(n1, n2)
                print(f"{n1} + {n2} = {result}")
            elif operator == "-":
                result += sub(n1, n2)
                print(f"{n1} - {n2} = {result}")
            elif operator == "*":
                result += mul(n1, n2)
                print(f"{n1} * {n2} = {result}")
            elif operator == "/":
                result += div(n1, n2)
                print(f"{n1} / {n2} = {result}")
            else:
                result += exp(n1, n2)
                print(f"{n1} ^ {n2} = {result}")

        else:
            break


