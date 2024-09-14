def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Welcome to the Simple Calculator!")

    # Input: First number
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Input: Second number
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Input: Operation choice
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        choice = input("Enter your choice (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid choice. Please select a valid operation.")

    # Perform the calculation
    if choice == '1':
        result = add(num1, num2)
        operation = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = '*'
    elif choice == '4':
        result = divide(num1, num2)
        operation = '/'

    # Display the result
    if isinstance(result, str):
        print(result)
    else:
        print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()
