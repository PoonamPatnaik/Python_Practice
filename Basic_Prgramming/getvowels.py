def get_vowels(test_string):
    vowels = "aeiouAEIOU"
    vowel_list = [char for char in test_string if char in vowels]
    return vowel_list
get_vowel = get_vowels("TestString")
print(get_vowel)