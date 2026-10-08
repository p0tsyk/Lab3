summa = float(input("Введите сумму покупки (руб): "))

if summa < 0:
    print("Ошибка: сумма не может быть отрицательной")
else:
    if summa > 1000:
        discount = 5
    elif summa > 500:
        discount = 3
    else:
        discount = 0

    itog = summa - summa * discount / 100
    print(f"Сумма покупки: {summa} руб")
    print(f"Скидка: {discount}%")
    print(f"К оплате: {itog} руб")