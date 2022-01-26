def game_instruct(): #выводит инструкцию
   print("\n\t\t\t\t\t Добро пожаловать в игру крестики-нолики.\n\n"
          "\tВ игре принимают участие два человека. Что бы сделать ход, надо через пробел,\n"
          "\tввести числа от 0 до 2, обозначающие координаты клетки игрового поля.\n "
          "\tПервое - значение строки, второе - столбца.\n"
          "\tВыигрывает тот кто первый заполнит своим символом любую вертикаль, горизонталь или диагональ игрового поля\n\n")
   print("\t\t\t\t\t\t Игровое поле представленно ниже\n")
   print("\t\t\t\t\t\t\t\t   0  1  2 ")
   print("\t\t\t\t\t\t\t\t 0 -  -  - ")
   print("\t\t\t\t\t\t\t\t 1 -  -  - ")
   print("\t\t\t\t\t\t\t\t 2 -  -  - ")

game_instruct()


input("\n\n\t\t\t\t\tДля начала игры нажмите Enter:")
print("\n\n")
field = [[" - "," - "," - "] for i in range(3)]

def g_field(): # Выводит игровое поле
   print("\t\t\t\t\t\t\t   0   1   2")

   for i in range(3):
      print (f"\n\t\t\t\t\t\t\t{i} {field[i][0]} {field[i][1]} {field[i][2]}")




def check():  #Проверка правильности ввода данных
    while True:
        coord = input("\t\tВведите через пробел кординаты(строка, столбец):").split()
        if len(coord) == 2:
            x, y = coord
            if (x.isdigit()) and (y.isdigit()):
                x, y = int(x), int(y)
                if 0 <= x <= 2 and 0 <= y <= 2:
                    if field[x][y] == " - ":
                        return x, y
                    else:
                        print(" Поле уже занято!!!")
                else:
                    print("Координаты вне диапазона!!!")
            else:
                print("Вводите только числа!!!")
        else:
            print("Надо вводить два числа!!!")


def victory():  # Проверка выигрыша

    for i in range(3):
        vic = []
        for j in range(3):
            vic.append(field[i][j])
        if vic == [" X "," X "," X "] or vic == [" 0 "," 0 "," 0 "]:
                print("\n\t\t\t\t\t\tП O Б Е Д А  !!!!!!!!!!!!!!!!\n")
                return True


    for i in range(3):
        vic = []
        for j in range(3):
            vic.append(field[j][i])
        if vic == [" X "," X "," X "] or vic == [" 0 "," 0 "," 0 "]:
                print("\n\t\t\t\t\t\tП O Б Е Д А  !!!!!!!!!!!!!!!!\n")
                return True

    vic = []
    for i in range(3):
        vic.append(field[i][i])
    if vic == [" X ", " X ", " X "] or vic == [" 0 ", " 0 ", " 0 "]:
            print("\n\t\t\t\t\t\tП O Б Е Д А  !!!!!!!!!!!!!!!!\n")
            return True

    vic = []
    for i in range(3):
        vic.append(field[i][2-i])
    if vic == [" X "," X "," X "] or vic == [" 0 "," 0 "," 0 "]:
            print("\n\t\t\t\t\t\tП O Б Е Д А  !!!!!!!!!!!!!!!!\n")
            return True
    return False


for num in range(1,10):

    g_field()

    if num % 2 == 1:
        print("\n\t    Ход ' X '")
    else:
        print("\t\t    Ход ' 0 '")

    x, y = check()

    if num % 2 == 1:
        field[x][y] = " X "
    else:
        field[x][y] = " 0 "

    if victory():
        g_field()
        break

    if num == 9:
        g_field()
        print("\n\n\t\t\t\t\t Н И Ч Ь Я - Победила дружба!!!!!! ")
