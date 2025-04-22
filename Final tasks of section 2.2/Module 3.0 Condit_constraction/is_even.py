def is_even(number):
    return "чётным" if number % 2 == 0 else "нечётным"

# Примеры использования функции
number1 = -2
result1 = is_even(number1)
print(f"Число {number1} является {result1}.")

number2 = 9
result2 = is_even(number2)
print(f"Число {number2} является {result2}.")
