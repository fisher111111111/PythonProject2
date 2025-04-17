def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):

        for j in range(0, n - i - 1):

            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

def main():
    while True:
        input_numbers = input("Введите числа через запятую: ")

        try:
            numbers = [int(num.strip()) for num in input_numbers.split(',')]
            break  # Ввод корректен, выходим из цикла
        except ValueError:
            print("Пожалуйста, введите только целые числа, разделенные запятыми.")

    bubble_sort(numbers)

    print("Отсортированный список:", end=' ')
    for i in range(len(numbers)):
        if i < len(numbers) - 1:
            print(numbers[i], end=', ')
        else:
            print(numbers[i])


if __name__ == "__main__":
    main()
