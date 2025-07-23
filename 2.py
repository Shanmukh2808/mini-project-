def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Main code
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operation = input("Choose (+, -, *, /): ")

if operation == '+':
    print("Result:", add(x, y))
elif operation == '-':
    print("Result:", subtract(x, y))
elif operation == '*':
    print("Result:", multiply(x, y))
elif operation == '/':
    print("Result:", divide(x, y))
else:
    print("Invalid operation")
