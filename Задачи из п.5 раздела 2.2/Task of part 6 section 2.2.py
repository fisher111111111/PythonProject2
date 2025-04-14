#Задача 1: Добавление элемента в список
numbers = [1, 2, 3]

print("Исходный список:", numbers)

numbers.append(4)

print("После выполнения операции:", numbers)

#Задача 2:  Удаление элемента из списка
capitals = ["Москва", "Лондон", "Париж"]

print("Исходный список:", capitals)

capitals.remove("Лондон")

print('После удаления "Лондон":', capitals)

#Задача 3: Доступ к элеменry по индексу
cities = ["Москва", "Питер", "Новосибирск", "Екатеринбург"]

element = cities[2]

print("Элемент с индексом 2:", element)

#Задача 4: Доступ к элементу по срезу списка
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
slice_of_numbers = numbers[3:7]

print("Срез элементов с индекса 3 до 7:", slice_of_numbers)

#Задача 5: Изменение элемента списка
colors = ["red", "green", "blue"]
colors[1] = "yellow"

print("Обновлённый список:", colors)

#Задача 6: Узнаем длину списка
animals = ["cat", "dog", "rabbit", "hamster"]
length_of_list = len(animals)

print("Длина списка равна", length_of_list)

#Задача 7: Добавление элемента в словарь
student = {"name": "Ivan", "age": 20}

print("Исходный словарь:", student)

student["grade"] = "A"

print("После добавления:", student)

#Задача 8: Изменение элемента словаря
student = {"name": "Ivan", "age": 20, "grade": "B"}

print("До изменения:", student)

student["grade"] = "A"

print("После изменения:", student)

#Задача 9: Удаление элемента из словаря
student = {"name": "Ivan", "age": 20, "grade": "A"}

print("Исходный словарь:", student)

del student["age"]

print("После удаления 'age':", student)

#Задача 10: Доступ к элементу словаря по ключу
student = {"name": "Ivan", "age": 20, "grade": "A"}
name_value = student["name"]

print(f"Имя студента: {name_value}")

#Задача 11: Проверка наличия ключа в словаре
student = {"name": "Ivan", "age": 20, "grade": "A"}
key_to_check = "grade"

if key_to_check in student:
    print(f"Ключ '{key_to_check}' найден в словаре.")

else:
    print(f"Ключ '{key_to_check}' не найден в словаре.")

#Задача 12: Изменение элемента во вложенном словаре
student = {
    "name": "Ivan",
    "address": {
        "city": "Moscow",
        "street": "Lenina"
    }
}

print("До изменения:", student)

student["address"]["city"] = "Saint Petersburg"

print("После изменения:", student)

#Задача 13: Изменение элемента в списке, находящемся в словаре
student = {
    "name": "Maria",
    "grades": [75, 82, 90]
}

print("До изменения:", student)

student["grades"][0] = 85

print("После изменения:", student)

#Задача 14: Изменение элемента в словаре, находящемся внутри списка
students = [
    {"name": "Ivan", "age": 20},
    {"name": "Petya", "age": 22}
]

print("До изменения:", students)

for student in students:
    if student["name"] == "Petya":
        student["age"] = 23

print("После изменения:", students)

#Задача 15: Проверка наличия элемента и определение длины кортежа
colors = ("red", "green", "blue")

is_green_present = "green" in colors

tuple_length = len(colors)

print(f"Наличие 'green': {is_green_present}. Длина кортежа: {tuple_length}")
