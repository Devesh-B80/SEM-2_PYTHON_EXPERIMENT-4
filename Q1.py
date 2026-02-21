"""1.  Write a program to count and display the number of capital letters in a given string."""

text = input("Enter a string: ")

capital_count = 0  # counter for uppercase letters

# Loop through each character
for ch in text:
    # Check ASCII range for capital letters
    if 'A' <= ch <= 'Z':
        capital_count += 1

# Print the final count
print("Number of capital letters:", capital_count)