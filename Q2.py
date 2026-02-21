""" Count total number of vowels in a given string. """
# Program to count total number of vowels in a given string

# Take input from the user
text = input("Enter a string: ")

# Initialize vowel counter
vowel_count = 0

# Define vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Traverse each character in the string
for ch in text:
    # Check if the character is a vowel
    if ch in vowels:
        vowel_count += 1  # increment counter

# Display the result
print("Total number of vowels:", vowel_count)