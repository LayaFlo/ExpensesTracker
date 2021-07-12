handle = open("strings.txt", "r")
content = handle.readlines()
for i in content:
    if i.rstrip().isalnum():
        print(i.rstrip(), "was ok.")
    else:
        print(i.rstrip(), "was invalid.")
handle.close()
