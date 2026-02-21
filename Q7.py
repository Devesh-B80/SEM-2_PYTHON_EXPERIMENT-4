"""Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
a) Fruits which are in both sets s1 and s2
b) Fruits only in s1 but not in s2
c) Count of all fruits from s1 and s2"""
# Program to create two sets of fruits and perform set operations

# Take number of fruits for each set
n = int(input("Enter number of fruits in each set: "))

# Initialize empty sets
s1 = set()
s2 = set()

print("Enter fruits for Set 1:")
for _ in range(n):
    fruit = input().strip()
    s1.add(fruit)  # add fruit to set 1

print("Enter fruits for Set 2:")
for _ in range(n):
    fruit = input().strip()
    s2.add(fruit)  # add fruit to set 2

# a) Fruits common in both sets (intersection)
common_fruits = s1.intersection(s2)

# b) Fruits only in s1 but not in s2 (difference)
only_s1 = s1.difference(s2)

# c) Count of all fruits from s1 and s2 (union)
all_fruits = s1.union(s2)
total_count = len(all_fruits)

# Display results
print("\nFruits in both sets:", common_fruits)
print("Fruits only in s1:", only_s1)
print("Total distinct fruits in s1 and s2:", total_count)