"""Given a string containing both upper and lower case alphabets. Write a Python program
to count the number of occurrences of each alphabet (case insensitive) and display the
same.
Sample Input
ABaBCbGc
Sample Output
2A
3B
2C
1G"""
# Program to count occurrences of each alphabet (case insensitive)

# Take input string
text = input("Enter a string: ")

# Convert the string to uppercase to make counting case-insensitive
text = text.upper()

# Dictionary to store frequency of each alphabet
freq = {}

# Traverse each character in the string
for ch in text:
    # Consider only alphabets
    if 'A' <= ch <= 'Z':
        # Update count in dictionary
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

# Display results in sorted order (A to Z)
for key in sorted(freq):
    print(freq[key], key, sep="")