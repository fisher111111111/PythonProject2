def check_number(number):
    if number > 0:
        if number % 2 == 0:
            return f"Число {number} положительное и чётное."
        else:
            return f"Число {number} положительное и нечётное."
    else:
        return f"Число {number} отрицательное."

result1 = check_number(8)
print(result1)

result2 = check_number(5)
print(result2)

result3 = check_number(-3)
print(result3)
