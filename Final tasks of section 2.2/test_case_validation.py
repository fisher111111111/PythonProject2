def get_positive_integer():
    while True:
        user_input = input("Введите количество тест-кейсов: ")
        if user_input.strip():
            try:
                value = int(user_input)
                if value > 0:
                    return value
                else:
                    print("Некорректный ввод. Введите положительное число.")
            except ValueError:
                print("Некорректный ввод. Введите положительное число.")
        else:
            print("Некорректный ввод. Введите положительное число.")


def main():
    test_cases = get_positive_integer()

    if test_cases > 10:
        print("Отличная работа!")
    else:
        print("Попробуйте улучшить результат.")


if __name__ == "__main__":
    main()
