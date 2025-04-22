def check_string_length(string, length):
    if len(string) > length:
        return f'Длина строки "{string}" достаточная.'
    else:
        return f'Длина строки "{string}" слишком короткая.'

# Примеры вызова функции
result1 = check_string_length("Python", 5)
print(result1)

result2 = check_string_length("Hi", 5)
print(result2)
