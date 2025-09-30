num1: int = int(input("Enter First Number: "))
num2: int = int(input("Enter Second Number: "))
op = input("Enter the operation to be performed")


def calculate(number1, number2, operator):
    if operator == "+":
        result = number1 + number2
        print(result)
    elif operator == "-":
        result = number1 - number2
        print(result)
    elif operator == "*":
        result = number1 * number2
        print(result)
    elif operator == "/":
        if number2 != 0:
            result = number1 / number2
            print(result)
        else:
            print("Division by 0 is not allowed")
    else:
        print("Invalid Operator use(+ | - | * | /)")


calculate(num1, num2, op)
