print("Calculator")

promtForNumbers = True

while True:
    if promtForNumbers:
        num1 = int(input("Give the first number: "))
        num2 = int(input("Give the second number: "))
        promtForNumbers = False
    print("""(1) +
(2) -
(3) *
(4) /
(5) Change numbers
(6) Quit
Current numbers:""", num1, num2)
    operator = int(input("Please select something (1-6): "))

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
    elif operator == 5:
        promtForNumbers = True
    elif operator == 6:
        print("Thank you!")
        break
