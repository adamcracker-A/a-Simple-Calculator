a = int(input("enter the first number: "))
op = input("enter an operator (+, -, /, *, ^, %): ")
b = int(input("enter the second number: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    try:
        print(a / b)
    except ZeroDivisionError:
        print("you can't devide by zero")
elif op == "^":
    print(a ** b)
elif op == "%":
    try:
        print(a % b)
    except ValueError:
        print("try again")