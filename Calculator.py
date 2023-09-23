def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

print("Simple Calculator")
print("Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter operation choice: ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            print("Result:", result)
        elif choice == '2':
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == '3':
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == '4':
            result = divide(num1, num2)
            print("Result:", result)
    else:
        print("Invalid choice. Please choose a valid operation.")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if another_calculation != 'yes':
        break
