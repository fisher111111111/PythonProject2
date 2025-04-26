def is_unique_list(lst):
    return len(lst) == len(set(lst))


print(is_unique_list([1, 2, 3, 4]))
print(is_unique_list([1, 2, 2, 3]))
