# 1. Создаем список с заданными значениями
list_numbers = [4, 7, 9, 2, 5]
tuple_numbers = (4, 7, 9, 2, 5)

# Выводим исходные данные
print("Исходный список:", list_numbers)
print("Исходный кортеж:", tuple_numbers)

# 2. Попытка изменить второй элемент в списке и кортежe
list_numbers[1] = 10  # Изменяем второй элемент в списке
print("Измененный список:", list_numbers)

try:
    tuple_numbers[1] = 10  # Попытка изменить второй элемент в кортеже
except TypeError:
    print("Ошибка: Кортеж нельзя изменить!")


list_numbers.append(6)
print("Добавленный элемент в список:", list_numbers)


try:
    raise TypeError("В кортеж нельзя добавить элемент!")
except TypeError as e:
    print("Ошибка:", e)
