import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
print("These are the 10 random numbers between 1 to 100:",random_numbers)
double_even_numbers = []
for even in random_numbers:
    if even % 2 == 0:
        double_even_numbers.append(even * 2)

print("Here is your even numbers doubled list from the original:", double_even_numbers)