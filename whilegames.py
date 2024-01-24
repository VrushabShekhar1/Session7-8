import random
lives = 3

while lives: #you dont need to mention > 0, since numbers that are not 0 are taken to be True
        print("you have", lives, "lives left")
        dice_roll = random.randint(1, 6)
        if dice_roll == 6:
            print("you rolled a 6, you win!")
            break # takes it out the while loop
        #you dont need the else statment here, cause the break takes it out
            print("you rolled a", dice_roll, "try again")
            lives -= 1

    if lives == 0:
        print("You lost all your lives, game over")

while True:
    print("You have", lives, "lives left")
    dice_roll = random.randint(1,6)
    if lives ==