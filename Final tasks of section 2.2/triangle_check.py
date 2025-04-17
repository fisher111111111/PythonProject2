def check_triangle(a, b, c):
    # Проверка условия существования треугольника
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


def triangle_type(a, b, c):
    if a == b == c:
        return "равносторонний"
    elif a == b or a == c or b == c:
        return "равнобедренный"
    else:
        return "разносторонний"


def main():
    a = float(input("Введите длину первой стороны: "))
    b = float(input("Введите длину второй стороны: "))
    c = float(input("Введите длину третьей стороны: "))

    if check_triangle(a, b, c):
        result = triangle_type(a, b, c)
        print(f"Результат: Треугольник {result}.")
    else:
        print("Результат: Треугольник не существует.")


if __name__ == "__main__":
    main()
