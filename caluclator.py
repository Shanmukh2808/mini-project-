def calculator():
    print("Select operation: +, -, *, /")
    op = input("Enter operation: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if op == '+':
        print(f"Result: {a + b}")
    elif op == '-':
        print(f"Result: {a - b}")
    elif op == '*':
        print(f"Result: {a * b}")
    elif op == '/':
        if b != 0:
            print(f"Result: {a / b}")
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operation")

calculator()
