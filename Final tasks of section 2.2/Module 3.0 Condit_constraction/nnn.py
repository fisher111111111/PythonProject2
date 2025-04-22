def check_grade(score):
    if 90 <= score <= 100:
        return "Отлично"
    elif 75 <= score < 90:
        return "Хорошо"
    elif 50 <= score < 75:
        return "Удовлетворительно"
    else:
        return "Неудовлетворительно"

score = 98.22

result = check_grade(score)
print(f"Оценка за {score} баллов: {result}.")
