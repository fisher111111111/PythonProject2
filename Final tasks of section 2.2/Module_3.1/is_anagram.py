def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())


print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
