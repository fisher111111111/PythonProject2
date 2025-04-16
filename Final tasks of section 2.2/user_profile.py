# Учимся  создавать, изменять и использовать переменные в Python.
# При создании функции для ввода и проверки данных не обошлось без читтерства
def input_with_validation(prompt):
    user_input = input(prompt)
    if not user_input:
        print("Ошибка: ввод не может быть пустым. Попробуйте снова!")
        return input_with_validation(prompt)
    return user_input

name = input_with_validation("Введите ваше имя: ")
profession = input_with_validation("Введите вашу профессию: ")
tool = input_with_validation("Введите ваш любимый инструмент для тестирования: ")

print(f"\nВаши данные:") # тут открыл для себя новый символ и его возможности переноса строки
print(f"Имя: {name}")
print(f"Профессия: {profession}")
print(f"Ваш любимый инструмент для тестирования: {tool}")