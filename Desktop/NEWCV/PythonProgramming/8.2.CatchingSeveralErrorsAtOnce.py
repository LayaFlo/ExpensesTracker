def openfile():
    filename = input("Give the file name: ")
    try:
        handle = open(filename, "r")
        content = handle.read()
        handle.close()
        return content
    except IOError:
        return False


def convertcontent(content):
    try:
        content = int(content)
        return content
    except Exception:
        return False


def main():
    result = openfile()
    if result == False:
        print("There seems to be no file with that name.")
    elif convertcontent(result) == False:
        print("The file contents were unsuitable.")
    else:
        print("The result was", 1000/convertcontent(result))


if __name__ == "__main__":
    main()
