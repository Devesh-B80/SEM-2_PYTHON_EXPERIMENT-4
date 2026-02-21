""" WAP to enter a string and a substring. You have to print the number of times that the
substring occurs in the given string. String traversal will take place from left to right, not
from right to left.
Sample Input
ABCDCDC
CDC
Sample Output
2"""
# Program to count how many times a substring occurs in a string
# Traversal is from left to right

# Take inputs from user
main_str = input("Enter the main string: ")
sub_str = input("Enter the substring: ")

count = 0  # counter for occurrences
sub_len = len(sub_str)

# Traverse the main string from left to right
for i in range(len(main_str) - sub_len + 1):
    # Check if substring matches the slice of main string
    if main_str[i:i + sub_len] == sub_str:
        count += 1  # increment if match found

# Display result
print(count)