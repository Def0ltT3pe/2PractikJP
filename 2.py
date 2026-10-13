def fmt(value):
    """Выводит число без лишних нулей: 36 -> 36, 96.8 -> 96.8, 6.21371 -> 6.21."""
    value = round(value, 2)
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.2f}".rstrip("0").rstrip(".")
prompts = {
    1: "Введите температуру: ",
    2: "Введите расстояние в километрах: ",
    3: "Введите массу в килограммах: ",
    4: "Введите длину в метрах: ",
    5: "Введите объем в литрах: ",
    6: "Введите объем в мегабайтах: "
}

while True:
    print("Выберите конвертер:")
    print("1. Градус Цельсия - Градус Фаренгейта")
    print("2. Километры - Мили")
    print("3. Килограммы - Фунты")
    print("4. Метры - Футы")
    print("5. Литры - Галлоны")
    print("6. Мегабайты - Гигабайты")

    try:
        n = int(input("Ваш выбор: "))
    except ValueError:
        print("Ошибка: нужно ввести целое число от 1 до 4!")
        exit()

    if n < 1 or n > 6:
        print("Ошибка: неизвестный номер преобразования! Допустимы только 1, 2, 3, 4.")
        exit()

    try:
        value = float(input(prompts[n]))
    except ValueError:
        print("Ошибка: нужно ввести число (можно с десятичной частью).")
        exit()

    if n == 1:
        result = value * 9 / 5 + 32
        print(f"{fmt(value)} C = {fmt(result)} F")
    elif n == 2:
        result = value * 0.621371
        print(f"{fmt(value)} км = {fmt(result)} миль")
    elif n == 3:
        result = value * 2.20462
        print(f"{fmt(value)} кг = {fmt(result)} фунтов")
    elif n == 4:
        result = value * 3.28084
        print(f"{fmt(value)} м = {fmt(result)} футов")
    elif n == 5:
        result = value *  0.264172
        print(f"{fmt(value)} л = {fmt(result)} галлонов")
    elif n == 6:
        result = value / 1024
        print(f"{fmt(value)} Мб = {fmt(result)} Гб")
    if input("Выполнить ещё одно преобразование? (да/нет):").lower() != "да":
        print("Программа завершена")
        break
