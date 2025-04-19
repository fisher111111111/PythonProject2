# log_processing.py

def main():

    log_line = input("Введите строку лога: ")

    processed_line = log_line.strip().replace("Ошибка", "Ошибка критическая")

    words = processed_line.split()

    print("Обработанная строка:", processed_line)
    print("Разбитый текст:", words)

if __name__ == "__main__":
    main()

