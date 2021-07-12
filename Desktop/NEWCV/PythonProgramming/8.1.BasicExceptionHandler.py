text = input("Give a number: ")


try:
    text = int(text)
    print("The input was suitable!")
except Exception:
    print("The input was malformed.")
