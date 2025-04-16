# Освоtybt работs с числами, списками и базовыми математическими операциями.

def main():
    # Запрос количества тест-кейсов за каждый день недели
    test_cases_per_day = []

    for day in ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]:
        while True:
            try:
                tests = int(input(f"Введите количество тест-кейсов за {day}: "))
                if tests < 0:
                    print(
                        "Количество тест-кейсов не может быть отрицательным. Пожалуйста, введите неотрицательное число.")
                else:
                    test_cases_per_day.append(tests)
                    break
            except ValueError:
                print("Пожалуйста, введите целое число.")

    # Вычисляем общее количество тестов и среднее количество тестов в день
    total_tests = sum(test_cases_per_day)
    average_tests = total_tests / len(test_cases_per_day)

    print(f"\nОбщее количество тестов за неделю: {total_tests}")
    print(f"Среднее количество тестов в день: {average_tests:.2f}")

    # Мотивационное сообщение
    if average_tests > 10:
        print("Отличная работа!")
    else:
        print("Попробуйте улучшить результат.")

if __name__ == "__main__":
    main()
