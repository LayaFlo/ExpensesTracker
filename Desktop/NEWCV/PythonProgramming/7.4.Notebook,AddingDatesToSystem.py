import time

while True:
    print("""(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit""")
    option = int(input("Please select one: "))

    if option == 1:
        handle = open("notebook.txt", "r")
        content = handle.read()
        print(content)
        handle.close()
    if option == 2:
        handle = open("notebook.txt", "a")
        content = input("Write a new note: ")
        curr_time = time.strftime("%X %x")
        handle.write(content + ":::" + curr_time + "\n")
        handle.close()
    if option == 3:
        handle = open("notebook.txt", 'w')
        handle.close()
        print("Notes deleted.")
    if option == 4:
        print("Notebook shutting down, thank you.")
        break
