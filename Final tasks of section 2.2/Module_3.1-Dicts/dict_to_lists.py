def dict_to_lists(my_dict):
    keys = list(my_dict.keys())
    values = list(my_dict.values())
    return (keys, values)


my_dict = {"a": 1, "b": 2, "c": 3}
print(dict_to_lists(my_dict))
