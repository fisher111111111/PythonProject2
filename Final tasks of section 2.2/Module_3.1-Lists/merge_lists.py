def merge_lists(list1, list2):
    merged_set = set(list1) | set(list2)
    return sorted(merged_set)


print(merge_lists([1, 2, 3], [3, 4, 5]))
