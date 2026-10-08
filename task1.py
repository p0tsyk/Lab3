height = float(input("Введите ваш рост (см): "))
weight = float(input("Введите ваш текущий вес (кг): "))

optimal = height - 100

if weight > optimal:
    print(f"Оптимальный вес: {optimal} кг")
    print(f"Рекомендация: снизить вес на {weight - optimal} кг")
elif weight < optimal:
    print(f"Оптимальный вес: {optimal} кг")
    print(f"Рекомендация: набрать вес на {optimal - weight} кг")
else:
    print(f"Ваш вес оптимален: {optimal} кг")