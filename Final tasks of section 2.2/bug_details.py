# bug_details.py

# Создаем cловарь с информацией о баге
bug_reports = {
    1: {
        "title": "Ошибка валидации формы",
        "status": "Открыт"
    }
}

def display_bug_report(bug_id):

    bug = bug_reports.get(bug_id)
    if bug:
        print(f"ID: {bug_id}\nНазвание: {bug['title']}\nСтатус: {bug['status']}")
    else:
        print("Баг не найден.")


def change_bug_status(bug_id, new_status):

    if bug_id in bug_reports:
        bug_reports[bug_id]["status"] = new_status
        print(f"Статус баг-репорта {bug_id} изменён на '{new_status}'")
    else:
        print("Баг с таким ID не найден.")

if __name__ == "__main__":

    bug_id = 1

    print("Текущая информация о баге:")
    display_bug_report(bug_id)

    change_bug_status(bug_id, "Закрыт")

    print("Обновленная информация о баге:")
    display_bug_report(bug_id)

