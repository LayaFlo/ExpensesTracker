import math


def getValidInput():
    while True:
        try:
            num = int(input("Give a number: "))
            break
        except:
            print("This input is invalid.")
            continue
    return num


print("Calculator")

promtForNumbers = True

while True:
    if promtForNumbers:
        num1 = getValidInput()
        num2 = getValidInput()
        promtForNumbers = False
    print("""(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7) Change numbers
(8) Quit
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
        result = math.sin(num1/num2)
        print("The result is: ", result)
    elif operator == 6:
        result = math.cos(num1/num2)
        print("The result is: ", result)
    elif operator == 7:
        promtForNumbers = True
    elif operator == 8:
        print("Thank you!")
        break
