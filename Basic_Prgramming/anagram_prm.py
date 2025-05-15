def are_anagrams(str1, str2):
    # Remove spaces and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if lengths are the same, if not, they can't be anagrams
    if len(str1) != len(str2):
        return False

    # Sort the characters in both strings and compare
    return sorted(str1) == sorted(str2)


# Example usage:
str1 = "listen "
str2 = "silent"

if are_anagrams(str1, str2):
    print(f"'{str1}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are NOT anagrams.")
