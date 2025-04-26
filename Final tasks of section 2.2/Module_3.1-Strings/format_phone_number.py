def format_phone_number(digits):
    if len(digits) != 10 or not digits.isdigit():
        return "Неверный формат ввода"
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"


print(format_phone_number("1234567890"))
