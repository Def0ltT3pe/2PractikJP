while True:
    print("Доступные операции: +, -, *, /, //, %, ^ (возведение в степень)")

    # Первое число
    while True:
        try:
            a = int(input("Введите первое число: "))
            break
        except ValueError:
            print("Ошибка: введите целое число. Попробуйте снова.")

    # Математическая операция
    c = input("Введите операцию: ").strip()

    # Второе число
    while True:
        try:
            b = int(input("Введите второе число: "))
            break
        except ValueError:
            print("Ошибка: введите целое число. Попробуйте снова.")

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '//': lambda x, y: x // y,
        '%': lambda x, y: x % y,
        '^': lambda x, y: x ** y,
    }
    if c in operations:
        try:
            result = operations[c](a, b)
            print("Результат:", result)
        except ZeroDivisionError:
            print("Ошибка: деление на ноль!")
    else:
        print("Ошибка: неизвестная операция")
    con= str(input("Хотите выполнить ещё одну операцию? (да/нет):"))
    if con=="да":
        continue
    else:
        print("Программа завершена")
        break
