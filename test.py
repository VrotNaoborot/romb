import pprint

a = [
    [' ', ' ', ' ', '*', ' ', ' ', ' '],
    [' ', ' ', '*', ' ', '*', ' ', ' '],
    [' ', '*', ' ', ' ', ' ', '*', ' '],
    ['*', ' ', ' ', '*', ' ', ' ', '*'],
    [' ', '*', ' ', ' ', ' ', '*', ' '],
    [' ', ' ', '*', ' ', '*', ' ', ' '],
    [' ', ' ', ' ', '*', ' ', ' ', ' ']
]





currentX = len(a) // 2
currentY = len(a) // 2

while (True):
    # лево
    leftX = currentX - 1
    leftY = currentY

    # левый верх
    leftUpX = currentX - 1
    leftUpY = currentY - 1

    # вверх
    UpX = currentX
    UpY = currentY - 1

    # правый верх
    RightUpX = currentX + 1
    RightUpY = currentY - 1

    # право
    rightX = currentX + 1
    rightY = currentY

    # правый низ
    DownRightX = currentX + 1
    DownRightY = currentY + 1

    # низ
    DownX = currentX
    DownY = currentY + 1

    # левый низ
    LeftDownX = currentX - 1
    LeftDownY = currentY + 1




    if a[leftUpY][leftUpX] == " ":
        currentX = leftUpX
        currentY = leftUpY
        a[currentY][currentX] = "*"
        continue

    elif a[UpY][UpX] == " ":
        currentX = UpX
        currentY = UpY
        a[currentY][currentX] = "*"
        continue

    elif a[RightUpY][RightUpX] == " ":
        currentX = RightUpX
        currentY = RightUpY
        a[currentY][currentX] = "*"
        continue

    elif a[rightY][rightX] == " ":
        currentX = rightX
        currentY = rightY
        a[currentY][currentX] = "*"
        continue

    elif a[DownRightY][DownRightX] == " ":
        currentX = DownRightX
        currentY = DownRightY
        a[currentY][currentX] = "*"
        continue

    elif a[DownY][DownX] == " ":
        currentX = DownX
        currentY = DownY
        a[currentY][currentX] = "*"
        continue

    elif a[LeftDownY][LeftDownX] == " ":
        currentX = LeftDownX
        currentY = LeftDownY
        a[currentY][currentX] = "*"
        continue

    elif a[leftY][leftX] == " ":
        currentX = leftX
        currentY = leftY
        a[currentY][currentX] = "*"
        continue

    else:
        break


pprint.pprint(a)