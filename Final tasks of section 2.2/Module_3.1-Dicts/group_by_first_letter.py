def group_by_first_letter(strings):
    result = {}
    for s in strings:
        if s:
            first_char = s[0]
            if first_char not in result:
                result[first_char] = []
            result[first_char].append(s)
    return result


strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))
