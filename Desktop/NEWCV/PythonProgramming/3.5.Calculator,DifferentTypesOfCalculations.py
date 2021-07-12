print("Calculator")
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))
operator = int(input("""(1) +
(2) -
(3) *
(4) /
Please select something (1-4): """))

if operator == 1:
    result = num1 + num2
    print("The result is: ", result)
elif operator == 2:
    result = num1 - num2
    print("The result is: ", result)
elif operator == 3:
    result = num1 * num2
    print("The result is: ", result)
elif operator == 4:
    result = num1 / num2
    print("The result is: ", result)
else:
    print("Selection was not correct.")
