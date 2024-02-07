print("Here will be the contents of the file: ")
num_aliens = 0
with open("x-files.txt", "r") as f:
    #inside here teh f file is open for reading
    #print(f.read())
    for line in f:
        num_aliens += line.count("alien")

#once I am out, the fiel is closed
print("the word alien shows up ", num_aliens, " times in the file")