def extract_subdict(my_dict, keys):
    return {k: my_dict[k] for k in keys if k in my_dict}

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]
print(extract_subdict(my_dict, keys))
