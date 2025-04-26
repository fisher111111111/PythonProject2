def merge_lists(list1, list2):
    return [list1[i] + list2[i] for i in range(len(list1))]


print(merge_lists([1, 2, 3], [4, 5, 6]))
