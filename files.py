f = open("x-files.txt", "a") # "a" is used to amend the file information, "w" to write somethign new
while True:
    line = input("give me some text to put into the file: ")
    if line.lower() == "stop":
        break
    f.write(line + "\n")

#we need to close the file at the end
f.close()

with open("x-files.txt", "r") as f:
    #inside here the f file is open for reading
    print(f.read())

#once I am out , the file is closed
#f.read