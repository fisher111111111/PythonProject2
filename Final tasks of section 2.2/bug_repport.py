# bug_reports.py

bugs = [
    {"id": 1, "description": "Ошибка 1", "priority": "High"},
    {"id": 2, "description": "Ошибка 2", "priority": "Low"},
    {"id": 3, "description": "Ошибка 3", "priority": "Medium"},
    {"id": 4, "description": "Ошибка 4", "priority": "High"},
    {"id": 5, "description": "Ошибка 5", "priority": "Low"}
]

priority_order = {"High": 1, "Medium": 2, "Low": 3}


def add_bug(description, priority):
#Добавление нового бага в список
    new_id = len(bugs) + 1
    new_bug = {"id": new_id, "description": description, "priority": priority}
    bugs.append(new_bug)
    print(f'Баг добавлен: {new_bug}')


def remove_low_priority_bugs():
#Удаление багов с низким приоритетом
    global bugs
    bugs = [bug for bug in bugs if bug["priority"] != "Low"]
    print('Баги с низким приоритетом удалены.')


def get_priority(bug):
# получения приоритета бага
    return priority_order[bug["priority"]]


def sort_bugs():
#cортировка багов по приоритету
    bugs.sort(key=get_priority)
    print('Баги отсортированы по приоритету.')


def print_bugs():
#Вывод списка багов
    for bug in bugs:
        print(bug)

if __name__ == "__main__":
    print("Исходный список багов:")
    print_bugs()

    add_bug("Ошибка 6", "Medium")

    sort_bugs()

    remove_low_priority_bugs()

    print("\nОбновленный список багов:")
    print_bugs()
