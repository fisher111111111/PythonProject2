def power_of(number, exponent=2):
    result = number ** exponent  # Возводим число в степень
    return result


def main():
    # Пример вызова функции с двумя аргументами
    num1 = 2
    exp1 = 3
    result1 = power_of(num1, exp1)
    print(f"Число {num1} в степени {exp1} равно {result1}.")

    # Пример вызова функции с одним аргументом
    num2 = 4
    result2 = power_of(num2)
    print(f"Квадрат числа {num2} равен {result2}.")


if __name__ == "__main__":
    main()
