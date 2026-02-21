"""Take two sets and apply various set operations on them :
S1 = {Red ,yellow, orange , blue }
S2 = {violet, blue , purple}"""
# Program to perform various set operations on two sets

# Given sets
S1 = {"Red", "yellow", "orange", "blue"}
S2 = {"violet", "blue", "purple"}

# 1. Union → all unique elements from both sets
union_set = S1.union(S2)

# 2. Intersection → common elements in both sets
intersection_set = S1.intersection(S2)

# 3. Difference (S1 - S2) → elements only in S1
difference_s1 = S1.difference(S2)

# 4. Difference (S2 - S1) → elements only in S2
difference_s2 = S2.difference(S1)

# 5. Symmetric Difference → elements in either set but not both
symmetric_diff = S1.symmetric_difference(S2)

# Display results
print("Set S1:", S1)
print("Set S2:", S2)

print("\nUnion:", union_set)
print("Intersection:", intersection_set)
print("Difference (S1 - S2):", difference_s1)
print("Difference (S2 - S1):", difference_s2)
print("Symmetric Difference:", symmetric_diff)