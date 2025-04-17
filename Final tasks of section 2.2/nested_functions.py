def calculator():
    def get_number(prompt):
        return float(input(prompt))

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Ошибка! Деление на ноль."
        return x / y

    first_number = get_number("Введите первое число: ")
    second_number = get_number("Введите второе число: ")
    operation = input("Выберите операцию (+, -, *, /): ")

    if operation == '+':
        result = add(first_number, second_number)
    elif operation == '-':
        result = subtract(first_number, second_number)
    elif operation == '*':
        result = multiply(first_number, second_number)
    elif operation == '/':
        result = divide(first_number, second_number)
    else:
        result = "Ошибка! Неверная операция."

    return f"Результат: {result}"


if __name__ == "__main__":
    print(calculator())
