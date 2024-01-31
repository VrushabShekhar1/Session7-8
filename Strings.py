hi = "hello"
i = 0
while i < len(hi):
    print(hi[i])
    i+=1

#for the reverse order
while i<len(hi):
    print(hi[len(hi)-1-i])
    i+=1
#SLICING
#Slicing includes the beginning of the slice and the ending excluded
base = "abscjsdfdifjls"
print("here are some slices")
print(base[0:3])
print(base[10:]) #all the way till the end
print(base[:10]) #all the way from the beginning
print(base[:]) #the whole string
print(base[::2]) #every other letter
print(base[5:15:3]) #every third letter from the 5th to the 15th
print(base[::-1]) #the whole string backwards

#== is used to compare if 2 strings are equal. <,> performs alphabetical comaparison.
#a is the smallest and z is the biggest in the python ranking of alphabets
#uppercase letters are smaller than lowercase letters
#Whenever you find the first mismatch, code stops there
# method is closely linked with the data type it comes with i.e basically funcitons
#dir() gives the list with the methods available for an object

