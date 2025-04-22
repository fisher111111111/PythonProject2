def count_items(*args):
    return len(args)  # Возвращаем количество переданных аргументов


def main():

    count1 = count_items(1, 2, 3, 4, 5, 6, 7)
    print(f"Количество переданных элементов: {count1}.")

    count2 = count_items("apple", "banana", "cherry", "orange", "hammer")
    print(f"Количество переданных элементов: {count2}.")


if __name__ == "__main__":
    main()
