DISCOUNT_TABLE = (
    (15000, 15),
    (10000, 10),
    (5000, 5),
)

CURRENCY = "руб."


def format_money(value):
    """Печатает целые суммы без копеек, а дробные — с двумя знаками."""
    value = round(value, 2)
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.2f}"


def get_discount_percent(subtotal):
    """Возвращает процент скидки для суммы покупки."""
    for threshold, percent in DISCOUNT_TABLE:
        if subtotal >= threshold:
            return percent
    return 0


def main():
    print("=" * 40)
    print("Расчёт стоимости покупки")
    print("=" * 40)
    print("Скидки: 5000-9999 -> 5%, 10000-14999 -> 10%, от 15000 -> 15%")

    while True:
        # Собираем товары одной покупки в список
        items = []
        while True:
            name = input("Введите название товара: ").strip()
            if not name:
                print("Ошибка: название не может быть пустым.")
                continue

            try:
                price = float(input("Введите цену: ").strip().replace(",", "."))
            except ValueError:
                print("Ошибка: цена должна быть числом.")
                continue
            if price <= 0:
                print("Ошибка: цена должна быть больше нуля.")
                continue

            try:
                quantity = int(input("Введите количество: ").strip())
            except ValueError:
                print("Ошибка: количество должно быть целым числом.")
                continue
            if quantity <= 0:
                print("Ошибка: количество должно быть больше нуля.")
                continue

            items.append((name, price, quantity))

            answer = input("Добавить ещё один товар? (да/нет): ").strip().lower()
            if answer != "да":
                break

        # Считаем общую стоимость
        print()
        subtotal = 0
        for name, price, quantity in items:
            item_sum = price * quantity
            subtotal += item_sum
            print(f"{name}: {format_money(item_sum)}")

        percent = get_discount_percent(subtotal)
        discount = subtotal * percent / 100
        total = subtotal - discount

        print(f"Общая стоимость: {format_money(subtotal)}")
        print(f"Скидка: {percent}%")
        print(f"Размер скидки: {format_money(discount)}")
        print(f"Итоговая стоимость: {format_money(total)}")

        answer = input("\nПосчитать ещё одну покупку? (да/нет): ").strip().lower()
        if answer != "да":
            print("Программа завершена")
            break


if __name__ == "__main__":
    main()