# number_sum.py
n = int(input("Введите число: "))

total_sum = 0

numbers = []

for i in range(1, n + 1):
    numbers.append(str(i))
    total_sum += i

print("Числа:", ' '.join(numbers))

print("Сумма чисел:", total_sum)
