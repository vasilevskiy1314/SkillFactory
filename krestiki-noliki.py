table = [0, 1, 2, 3, 1, "-", "-", "-", 2, "-", "-", "-", 3, "-", "-", "-"]

# функция отрисовки поля:
def draw(table):
    for i in range (4):
        print(table[0+i*4], table[1+i*4], table[2+i*4], table[3+i*4])

# функция записывающая ход 1го игрока:
def hod1():
    print("\nХод игрока 1 (X)!")
    cifra = int(input("Введите номер ряда от 1 до 3 (цифры по вертикали): "))
    while not 1 <= cifra <= 3:
        cifra = int(input("Вы неправильно ввели число! Введите номер ряда от 1 до 3: "))
    bukva = int(input("Введите номер колонки (цифры по горизонтали): "))
    while not 1 <= bukva <= 3:
        bukva = int(input("Вы неправильно ввели число! Введите номер колонки от 1 до 3: "))
    if cifra == 1:
        table[4+bukva] = "X"
    elif cifra == 2:
        table[8 + bukva] = "X"
    elif cifra == 3:
        table[12 + bukva] = "X"
    return (draw(table))

# функция записывающая ход 2го игрока:
def hod2():
    print("\nХод игрока 2 (O)!")
    cifra = int(input("Введите номер ряда от 1 до 3 (цифры по вертикали): "))
    while not 1 <= cifra <= 3:
        cifra = int(input("Вы неправильно ввели число! Введите номер ряда от 1 до 3: "))
    bukva = int(input("Введите номер колонки (цифры по горизонтали): "))
    while not 1 <= bukva <= 3:
        bukva = int(input("Вы неправильно ввели число! Введите номер колонки от 1 до 3: "))
    if cifra == 1:
        table[4+bukva] = "O"
    elif cifra == 2:
        table[8 + bukva] = "O"
    elif cifra == 3:
        table[12 + bukva] = "O"
    return (draw(table))

# функция проверки победы:
def win():
    if table[5] == table[6] == table[7] != "-" or table[9] == table[10] == table[11] != "-" or table[13] == table[14] == table[15] != "-" or table[5] == table[9] == table[13] != "-" or table[6] == table[10] == table[14] != "-" or table[7] == table[11] == table[15] != "-" or table[5] == table[10] == table[15] != "-" or table[7] == table[10] == table[13] != "-":
        return "Есть победитель!"
    else:
        return False

# функция описывающая ход игры:
def game():
    anyone_win = False
    while not anyone_win:
        hod1()
        if win():
            print("")
            print(win())
            print("Игрок №1 победил!")
            anyone_win = True
            break
        hod2()
        if win():
            print("")
            print(win())
            print("Игрок №2 победил!")
            anyone_win = True
            break

print(draw(table))
print(game())