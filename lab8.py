honey_positions = [
    ("Мёд липовый", 3, 1250),
    ("Мёд цветочный", 7, 1000),
    ("Мёд гречишный", 6, 1300),
    ("Донниковый мёд", 1, 1750),
    ("Малиновый мёд", 10, 2000),
]
def print_check(honey_positions):
    sum = 0  # переменная для накопления общей суммы
    print("ООО Мед\n")
    # в цикле будем выводить название, количество и цену
    for honey in honey_positions:
        name = honey[0]
        amount = honey[1]
        price = honey[2]
        print(f"{name} ({amount} шт.) - {price} тг.")
        sum += amount * price  # здесь же будем считать ещё и общую сумму
    print(f"\nИтого: {sum} тг.")
    print("Спасибо за покупку!")