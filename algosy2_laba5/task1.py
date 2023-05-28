mas = [[1, 0, 1],
       [0, 0, 1],
       [0, 1, 1]]  # пусть 1 - крестик, 0 - нолик


def kr_no(arr):
    win = False
    who_win = 0

    for i in range(len(arr)):
        k = 0
        for j in range(len(arr[i]) - 1):
            if arr[i][j] == arr[i][j+1]:
                k += 1
                who_win = arr[i][j]
        if k == 2:
            win = True
            return win, who_win
        k = 0
        for j in range(len(arr[i]) - 1):
            if arr[j][i] == arr[j+1][i]:
                k += 1
                who_win = arr[j][i]
        if k == 2:
            win = True
            return win, who_win

    k = 0
    r = 0
    for i in range(2):
        if arr[i][i] == arr[i+1][i+1]:
            k += 1
        if arr[i][2-i] == arr[i+1][1-i]:
            r += 1
    if k == 2:
        win = True
        who_win = arr[0][0]
    elif r == 2:
        win = True
        who_win = arr[0][2]
    return win, who_win


result = kr_no(mas)
if result[0]:
    print(str(result[1]) + ' won!')
else:
    print('nobody won :(')
