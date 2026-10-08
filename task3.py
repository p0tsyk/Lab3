a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))

if a == 1:
    a = 2
elif a % 2 == 0:
    a = a / 2

if b == 1:
    b = 2
elif b % 2 == 0:
    b = b / 2

if c == 1:
    c = 2
elif c % 2 == 0:
    c = c / 2

print("Результат:", a, b, c)