while True:
    while True:
        user_input = input("Введите число: ")
        try:
            num = int(user_input)
            break
        except ValueError:
            print("Ошибка! Введите целое число.")

    print("Ваше число:", num)

    #Положительное / отрицательное / ноль
    if num > 0:
        print("Положительное: да")
    else:
        print("Положительное: нет")

    #Является ли число квадратом целого числа
    root = int(num ** 0.5)
    if num >= 0 and root * root == num:
        print("Является квадратом целого числа")
    else:
        print("Не является квадратом целого числа")

    if num < 0:
        print("Отрицательное: да")
    else:
        print("Отрицательное: нет")

    if num == 0:
        print("Ноль: да")
    else:
        print("Ноль: нет")

    #Чётное
    if num % 2 == 0:
        print("Четное: да")
    else:
        print("Четное: нет")

    #Делится на 3
    if num % 3 == 0:
        print("Делится на 3: да")
    else:
        print("Делится на 3: нет")

    #Делится на 5
    if num % 5 == 0:
        print("Делится на 5: да")
    else:
        print("Делится на 5: нет")

    #Простое
    if num <= 1:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

    if is_prime:
        print("Простое: да")
    else:
        print("Простое: нет")

    #Количество цифр
    digit_count = len(str(abs(num)))
    print("Количество цифр:", digit_count)
    if input("Проверить ещё одно число? (да/нет):").lower() != "да":
        print("Программа завершена")
        break
