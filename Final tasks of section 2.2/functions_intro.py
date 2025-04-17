def greet_user(name):
    """Функция для приветствия пользователя."""
    print(f"Привет, {name}! Добро пожаловать в мир Python!")


def calculate_sum(a, b):
    """Функция для вычисления суммы двух чисел."""
    return a + b


def main():
    # Запрашиваем имя пользователя
    user_name = input("Введите ваше имя: ")
    greet_user(user_name)

    # Запрашиваем два числа у пользователя с проверкой на корректность ввода
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            break  # Если ввод успешный, выходим из цикла
        except ValueError:
            print("Ошибка: Пожалуйста, введите действительное числовое значение.")

    # Вычисляем сумму и выводим результат
    result = calculate_sum(num1, num2)
    print(f"Сумма чисел: {result}")


if __name__ == "__main__":
    main()
