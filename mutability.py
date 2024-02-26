# Lists are mutable
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Strings are immutable
my_string = "Hello"
print(my_string)  # Output: Hello
my_string[0] = "h"  # This will raise an error: TypeError: 'str' object does not support item assignment

# We can create a new string instead
my_string = "hello"
print(my_string)  # Output: hello
