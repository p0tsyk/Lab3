print("Вводите координаты клеток от 1 до 8")
kx = int(input("Король x: "))
ky = int(input("Король y: "))
rx = int(input("Ладья x: "))
ry = int(input("Ладья y: "))
bx = int(input("Слон x: "))
by = int(input("Слон y: "))


def on_board(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8


if not (on_board(kx, ky) and on_board(rx, ry) and on_board(bx, by)):
    print("Ошибка: координаты должны быть от 1 до 8")
elif (kx, ky) == (rx, ry) or (kx, ky) == (bx, by) or (rx, ry) == (bx, by):
    print("Ошибка: фигуры не могут стоять на одной клетке")
else:
    rook_threat = False
    bishop_threat = False

    if ry == ky:                      # одна горизонталь
        # слон перекрывает, если стоит на той же горизонтали между ними
        blocked = (by == ky) and (min(kx, rx) < bx < max(kx, rx))
        rook_threat = not blocked
    elif rx == kx:                    # одна вертикаль
        blocked = (bx == kx) and (min(ky, ry) < by < max(ky, ry))
        rook_threat = not blocked

    if abs(bx - kx) == abs(by - ky):  # одна диагональ
        # ладья перекрывает, если стоит на той же диагонали между ними
        blocked = (abs(rx - kx) == abs(ry - ky)
                   and (rx - kx) * (bx - kx) > 0
                   and (ry - ky) * (by - ky) > 0
                   and abs(rx - kx) < abs(bx - kx))
        bishop_threat = not blocked

    if rook_threat and bishop_threat:
        print("Король под боем: угроза от ладьи и от слона")
    elif rook_threat:
        print("Король под боем: угроза от ладьи")
    elif bishop_threat:
        print("Король под боем: угроза от слона")
    else:
        print("Король не под боем")