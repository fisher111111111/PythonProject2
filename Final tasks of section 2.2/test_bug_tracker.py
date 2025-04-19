# test_bug_tracker.py
bug_tracker = {'Анна': 3, 'Иван': 5, 'Дмитрий': 7}

tester_name = input("Введите имя тестировщика: ")

if tester_name in bug_tracker:
    bug_tracker[tester_name] += 1
else:
    bug_tracker[tester_name] = 1

print("Обновленные данные:", bug_tracker)
