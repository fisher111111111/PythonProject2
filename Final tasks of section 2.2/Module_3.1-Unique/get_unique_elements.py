def get_unique_elements(lst):
    unique_elements = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_elements.append(item)
            seen.add(item)
    return unique_elements


print(get_unique_elements([1, 2, 2, 3, 4, 4, 4, 5]))
