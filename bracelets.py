# if i HAVE an proper'
#    ty called "bracelet" that is a list of integers, and I want to find the number of unique bracelets that can be formed from the integers in the list. A bracelet is defined as a circular arrangement of beads, where the order of the beads matters but the starting point does not. For example, the bracelet [1, 2, 3] is considered the same as [2, 3, 1] and [3, 1, 2].
#
# To solve this problem, we can use a set to store the unique bracelets. We can generate all possible rotations of the bracelet and add them to the set. The size of the set will give us the number of unique bracelets.

# Here's a Python function to achieve this:     1
def count_unique_bracelets(bracelet):   
    unique_bracelets = set()
    n = len(bracelet)

    for i in range(n):
        rotated_bracelet = bracelet[i:] + bracelet[:i]
        unique_bracelets.add(tuple(rotated_bracelet))
    return len(unique_bracelets)
# Example usage of the function:
# bracelet = [1, 2, 3] 
bracelet = [1, 2, 3]
print("Number of unique bracelets:", count_unique_bracelets(bracelet))
# Output: Number of unique bracelets: 1
# The function works by generating all rotations of the input bracelet and storing them in a set to ensure uniqueness.
# The time complexity of this function is O(n^2) in the worst case, where n is the length of the bracelet. This is because we generate n rotations, and each rotation takes O(n) time to create. The space complexity is O(n) for storing the unique bracelets in the set.\




[3,6,1, 7,4,2,3]
[6,9,3,4]