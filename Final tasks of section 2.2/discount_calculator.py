# discount_calculator.py

total_amount = float(input("Введите сумму покупки: "))

discount_percentage = float(input("Введите процент скидки: "))

discount_amount = (discount_percentage / 100) * total_amount

final_amount = total_amount - discount_amount

final_amount_rounded = round(final_amount)

print(f"\nВы экономите: {discount_amount:.2f}")
print(f"Сумма к оплате (округлено): {final_amount_rounded}")
