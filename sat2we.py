def longest_palindrome(s):
    # If the string is empty or has one character, it's already a palindrome
    if len(s) < 2:
        return s

    longest = ""  # To store the longest palindrome found

    for i in range(len(s)):
        # Check for odd-length palindrome (centered at one character)
        odd = expand(s, i, i)
        # Check for even-length palindrome (centered between two characters)
        even = expand(s, i, i + 1)

        # Choose the longer one
        current_longest = odd if len(odd) > len(even) else even

        # Update the result if this is the longest so far
        if len(current_longest) > len(longest):
            longest = current_longest

    return longest

def expand(s, left, right):
    # Expand outward while characters match
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # Return the matching substring
    return s[left + 1:right]

# Example usage
print(longest_palindrome("babad"))  # Output: "bab" or "aba"
print(longest_palindrome("cbbd"))   # Output: "bb"
