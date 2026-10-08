a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Стороны должны быть положительными")
elif a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Треугольник равносторонний")
    elif a == b or b == c or a == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Такой треугольник не существует")