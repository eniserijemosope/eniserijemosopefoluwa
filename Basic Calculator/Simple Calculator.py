#simple python calculator


operator = input("Type in the basic operator you would like to use (+, -, /, *): ")

number1 = float(input("Input first number: "))
number2 = float(input("Input second number: "))

if operator == "":
    print("You didn't input an operator")
elif operator == "+":
    result = number2 + number1
    print(f"The sum total is {result}")
elif operator == "-":
    result = number1 - number2
    print(f"The sum total is {result}")
elif operator == "/":
    result = number1 / number2
    print(f"The sum total is {result}")
elif operator == "*":
    result = number2 + number1
    print(f"The sum total is {result}")
else:
    print(f"The operator {operator} isn't recognizd!.")


