def find_bob_pattern(text):
    # Initialize count of occurrences
    count = 0

    # Iterate over the text
    for i in range(len(text)):
        # Check if current character is "b"
        if text[i] == "b":
            # If we're not at the end of the string
            if i + 2 < len(text):
                # If the next character is not a space, and the character after that is "b"
                if text[i + 1] != " " and text[i + 2:i + 5] == "Bob":
                    # Increment count
                    count += 1

    return count

print(find_bob_pattern("I love ballllllisticBob but aBob does not bbob"))