filename = input("Give a file name: ")
writefile = open(filename, "w")

content = input("Write something: ")

writefile.write(content)
print("Wrote", content, "to the file", filename)
writefile.close()
