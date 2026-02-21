"""Program to count number of unique words in a given sentence using sets."""
# Program to count number of unique words in a given sentence using sets

# Take input sentence from the user
sentence = input("Enter a sentence: ")

# Convert sentence to lowercase to make counting case-insensitive
sentence = sentence.lower()

# Split sentence into words (default delimiter = space)
words = sentence.split()

# Convert list of words into a set to remove duplicates
unique_words = set(words)

# Count unique words
count = len(unique_words)

# Display result
print("Number of unique words:", count)