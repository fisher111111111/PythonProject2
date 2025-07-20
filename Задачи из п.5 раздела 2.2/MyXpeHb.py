# name = "Anna"
# a=5
# b=7
# def name_sum(name, sum):
#
#     print(f'Hello {name}, welcome to Pythons world!')
#     print(a+b)
#
# name_sum(name, sum)


#
# def greet_user(name):
#     print(f"Привет, {name}! Добро пожаловать в мир Python!")
#
# def calculate_sum(a, b):
#     return a + b
#
# name = input("Введите ваше имя: ")
# greet_user(name)
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
#
# result = calculate_sum(a, b)
# print(f"Сумма чисел: {result}")

# your_age=int(input("введите ваш год рождения:"))
# current_year=2025
# age=current_year-your_age
# print(f'Ваш возраст: {age}')
# if age < 18:
#     print("Вы еще молоды, учеба — ваш путь!")
# elif age > 65:
#     print("Пора наслаждаться заслуженным отдыхом!")
# else:
#     print("Отличный возраст для карьерного роста!")

# number = int(input("Введите число:"))
# for i in range (1,  number+1):
#     print(i, end=" ")
# print()
#
# total = sum (range(i, number+1))
# print(f"Сумма чисел: {total}")
# def приветствие(имя):    # имя — параметр функции
#     print("Привет, " + имя + "!")
#
# приветствие("Анна")     # "Анна" — аргумент, переданного в параметр имя
# q = 7
# a = 3
# def summ(q, a):
#     return q-a
# print(summ(q,a))

# def summ():
#     q = 7
#     a = 8
#     return q + a
#
# print(summ())
import requests


response = requests.post('https://restful-booker.herokuapp.com/auth', json={ "username" : "admin", "password" : "password123"})
# print(response.status_code)  # Выведет, например, 200 для успешного запроса
print(response.headers)  # Выведет словарь заголовков
print(response.text)


#
# response1 = requests.get('https://restful-booker.herokuapp.com/booking/848')
# assert response1.status_code == 200, "Статус-код  не соответствует ожидаемому"
# print(response1)
# print(response1.text)



