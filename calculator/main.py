# this is a simple command-line calculator in Python. This calculator will be able to perform basic arithmetic operations like addition, subtraction, multiplication, and division


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"


def calculator():
    print("\nSelect an operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("\nPlease input the number of the operation: "))

    if choice not in (1, 2, 3, 4):
        print("\nThat is not one of the operations, Please try again!")
        return

    num1 = float(input("Please input the first number: "))
    num2 = float(input("Please input the second number: "))

    match choice:
        case 1:
            add_answer = add(num1, num2)
            print(f"\nThe result of the addition is: {add_answer}")
        case 2:
            subtract_answer = subtract(num1, num2)
            print(f"\nThe result of the subtraction is: {subtract_answer}")
        case 3:
            multiply_answer = multiply(num1, num2)
            print(f"\nThe result of the multiplication is: {multiply_answer}")
        case 4:
            divide_answer = divide(num1, num2)
            if isinstance(divide_answer, int):
                print(f"\nThe result of the division is: {divide_answer}")
            else:
                print(divide_answer)


if __name__ == "__main__":
    print("\nCalculator")
    calculator()
