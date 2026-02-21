"""Input a sentence and print words in separate lines."""
# Program to input a sentence and print words on separate lines

# Take sentence input from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words using space as delimiter
words = sentence.split()

# Traverse and print each word on a new line
for word in words:
    print(word)