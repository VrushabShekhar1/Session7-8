import random

try:
    age = int(input("How old are you"))
except ValueError: #to avoid the age being in letters
    print ( " I am sorry, but that is not a valid number")
except ZeroDivisionError: #to avoid division by 0
    print(" I am sorry, but you cannot divide by zero")
else:
        #Do some sanity check on age
        if age < 0:
            print("I am sorry, your age cannot be negative")
        elif age > 130:
            print("I am sorry, but your age cannot be greater than 130")

drinks= ["beer", "whiskey", "wine", "campari", "rum", "gin", "vermouth"]
try:
    age = int(input("How old are you"))
    country = input("Where do you live")
except ValueError: #to avoid the age being in letters
    print ( " I am sorry, but that is not a valid number")
except ZeroDivisionError: #to avoid division by 0
    print(" I am sorry, but you cannot divide by zero")
else:
        #Do some sanity check on age
        if age < 0 or age > 130:
            print("I am sorry, your age cannot be negative")
        elif age < 18:
            print("I am sorry, but you are too young to play this drinking game everywhere")
        elif age < 21 and country == "US":
            print("I am sorry, too young to play this drinking game in the US")
        else:
            drink = random.choice
            print("take a shot of", drink, ". Thank you for playing, you are", age, "years old")
