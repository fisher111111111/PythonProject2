def get_unique_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    s = s.lower()
    return {char for char in s if char in vowels}


print(get_unique_vowels("Hello World"))
