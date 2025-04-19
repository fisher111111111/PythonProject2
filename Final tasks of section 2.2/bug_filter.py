# bug_filter.py

def main():

    bug_reports = [
        "Ошибка 1 – High",
        "Ошибка 2 – Medium",
        "Ошибка 3 – Low",
        "Ошибка 4 – High",
        "Ошибка 5 – Medium",
        "Ошибка 6 – Low",
        "Ошибка 7 – High"
    ]

    priority = input("Введите приоритет для поиска (High, Medium, Low): ").strip().capitalize()

    filtered_bugs = [bug for bug in bug_reports if priority in bug]

    if filtered_bugs:
        print("Найденные баги:")
        for bug in filtered_bugs:
            print(f"- {bug}")
    else:
        print("Нет багов с указанным приоритетом.")


if __name__ == "__main__":
    main()
