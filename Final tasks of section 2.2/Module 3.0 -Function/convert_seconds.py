def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return (hours, minutes)

def main():
    try:
        seconds_input = int(input("Введите количество секунд: "))
        hours, minutes = convert_seconds(seconds_input)
        print(f"В {seconds_input} секундах содержится {hours} час(ов) и {minutes} минут(ы).")
    except ValueError:
        print("Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()

