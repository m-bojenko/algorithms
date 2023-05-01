n = int(input('(количество экспонатов) N: '))  # количсетво экспонатов
m = int(input('(количество заходов) M: '))  # количество заходов
k = int(input('(килограмм за заход) K: '))  # килограмм за один заход
arr = []

#  Ввод данных об экспонатах
for i in range(n):
    b = [0, 0]
    a = input('Вес и цена: ').split()
    b[0] = int(a[0])
    b[1] = int(a[1])
    arr.append(b)
print(arr)

summa = 0
for h in range(m):  # Проходимся по количеству заходов
    if arr:
        work_list = []
        print('Заход ' + str(h + 1))
        work_list.append([])
        for j in range(k):
            if j + 1 >= arr[0][0]:
                work_list[0].append([arr[0][1], [arr[0]]])
            else:
                work_list[0].append([0, []])
        for i in range(1, len(arr)):  # проходимся по ещё не взятым экспонатам
            work_list.append([])
            for j in range(k):  # проходимся по количеству килограммов до К
                if i != 0:
                    if j + 1 < arr[i][0]:
                        work_list[i].append(work_list[i-1][j])
                    elif j + 1 == arr[i][0]:
                        if work_list[i-1][j][0] > arr[i][1]:
                            work_list[i].append(work_list[i-1][j])
                        else:
                            work_list[i].append([arr[i][1], [arr[i]]])
                    else:
                        if work_list[i-1][j][0] > arr[i][1] + work_list[i-1][j-arr[i][0]][0]:
                            work_list[i].append(work_list[i-1][j])
                        else:
                            temp = []
                            for o in work_list[i-1][j-arr[i][0]][1]:
                                temp.append(o)
                            temp.append(arr[i])
                            work_list[i].append([arr[i][1] + work_list[i-1][j-arr[i][0]][0], temp])
        summa += work_list[len(work_list) - 1][k - 1][0]
        for i in work_list[len(work_list) - 1][k - 1][1]:
            print(i)
            arr.pop(arr.index(i))
        print('Всего в этом заходе сумма: ' + str(work_list[len(work_list) - 1][k - 1][0]))
print('Общая сумма: ' + str(summa))
