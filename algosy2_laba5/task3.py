desk = []  # начальная доска из нулей
for i in range(8):
    desk.append([])
    for j in range(8):
        desk[i].append('0')


count = 0


def variant(mas, row=0):
    """ рекурсивная функция для нахождения вариантов расстановки """

    if row != 8:
        for i in range(8):
            if mas[row][i] == '0':
                temp = []
                for a in range(8):
                    temp.append([])
                    for j in range(8):
                        temp[a].append(mas[a][j])
                temp = change_mas(temp, row, i)
                variant(temp, row+1)
    else:
        for i in range(8):
            print(mas[i])
        print()
        global count
        count += 1


def change_mas(mas, row, column):
    """ функция заполняющая знаками "-" все элементы на
    диагоналях, столбцах и строках выбранного элемнта """

    for i in range(min(row, column)):
        mas[row-i-1][column-i-1] = '-'
    for i in range(7 - max(row, column)):
        mas[row+i+1][column+i+1] = '-'
    for i in range(min(7-column, row)):
        mas[row-i-1][column+i+1] = '-'
    for i in range(min(7-row, column)):
        mas[row+i+1][column-i-1] = '-'
    for i in range(8):
        for j in range(8):
            if i == row or j == column:
                mas[i][j] = '-'
    mas[row][column] = 'Ф'
    return mas


variant(desk)
print(count)
