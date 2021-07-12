def tester(text, givenstring="Too short"):
    result = len(text)
    if result >= 10:
        if "X" in text:
            print(text + "\nX spotted!")
        else:
            print(text)
    if result < 10:
        print(givenstring)


def main():
    while True:
        text = input("Write something (quit ends): ")
        if text == "quit":
            break
        else:
            tester(text)


if __name__ == "__main__":
    main()
