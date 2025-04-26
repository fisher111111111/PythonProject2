def longest_word(s):
    words = s.split()
    longest = max(words, key=len)
    return longest


print(longest_word("In the middle of a vast desert, an extraordinary adventure awaits"))  # extraordinary
