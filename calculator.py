def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Cannot divide by zero"

print("Simple Calculator")
print("Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = int(input("Enter the operation choice (1-4): "))

if operation == 1:
    result = add(num1, num2)
    print("Result:", result)
elif operation == 2:
    result = subtract(num1, num2)
    print("Result:", result)
elif operation == 3:
    result = multiply(num1, num2)
    print("Result:", result)
elif operation == 4:
    result = divide(num1, num2)
    print("Result:", result)
else:
    print("Invalid operation choice")
