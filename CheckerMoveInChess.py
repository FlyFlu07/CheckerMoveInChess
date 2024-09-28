# const
MaxBoardSize = 8
def GetCoordinatesAndFigure():
    coords = input("Введите начальную и  конечную точку\n")
    x_start, y_start, x_final, y_final = ord(coords[0]) - 64,  int(coords[1]), ord(coords[3]) - 64, int(coords[4])
    figure = input('Введите фигуру \n')  #Пешка, Ладья, Конь, Слон, Королева, Король
    return x_start, y_start, x_final, y_final, figure
GetCoordinatesAndFigure()



abs_x = abs(x_final - x_start)
abs_y = abs(y_final - y_start)



def CheckMoveForPawn(x_start, y_start, x_final, y_final):
    if x_start != x_final or y_start == MaxBoardSize:
        res = "Нельзя"
    elif y_start == 2:
        if 1 <= abs_y <= 3:
            res = "Можно"
        else: res = 'Нельзя'
    elif abs_y == 1:
        res = "Можно"
    else: res = 'Нельзя'
    return res
def CheckMoveForCastle(abs_x, abs_y):
    if abs_x == abs_x:
        res = "Можно"
    else:
        res = 'Нельзя'
    return res

def CheckMoveForHorse(abs_x, abs_y):
    if abs_x == 2 and abs_y == 1 or abs_x == 1 and abs_y == 2:
        res = "Можно"
    else:
        res = "Нельзя"
    return res

def CheckMoveForElephant(abs_x, abs_y):
    if abs_x == abs_y:
        res = "Можно"
    else:
        res = 'Нельзя'
    return res

def CheckMoveForKing(abs_x, abs_y):
    if abs_x <= 1 and abs_y <= 1:
        res = "Можно"
    else:
        res = 'Нельзя'
    return res


if figure == 'Ладья':
    CheckMoveForCastle(abs_x, abs_y)
elif figure == 'Пешка':
    CheckMoveForPawn(x_start, y_start, x_final, y_final)
elif figure == 'Слон':
    CheckMoveForElephant(abs_x, abs_y)
elif figure == 'Король':
    CheckMoveForKing(abs_x, abs_y)
elif figure == 'Королева':
    CheckMoveForElephant(abs_x, abs_y)
    if res == 'Нельзя': 
        CheckMoveForCastle(abs_x, abs_y)

else:
    res = "Неизвестная фигура"

print(res)

