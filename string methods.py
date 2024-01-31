text ="abcdefg"
print(dir(text))
help(text.isidentifier)
sentence = "Hello, kind-sir; how man! I be of service today?"
punctuation = ".,;!?-"
#santise the sentence
for p in punctuation:
    sentence = sentence.replace(p, "") #replace the punctuation with nothing
print(sentence)
#split the sentence into words
words = sentence.split(" ")
print(words)