def sort_rub_kg(arr):
    #  Сортировка по цене за килограмм
    arr2 = []
    n = len(arr)
    for i in range(n):
        max = arr[0]
        for j in arr:
            if j[2] > max[2]:
                max = j
        arr2.append(max)
        arr.pop(arr.index(max))
    return arr2


def sort_max_rub(arr):
    #  Сортировка по цене
    arr2 = []
    n = len(arr)
    for i in range(n):
        max = arr[0]
        for j in arr:
            if j[1] > max[1]:
                max = j
        arr2.append(max)
        arr.pop(arr.index(max))
    return arr2


n = int(input('N: '))  # количсетво экспонатов
m = int(input('M: '))  # количество заходов
k = int(input('K: '))  # килограмм за один заход
arr = []

#  Ввод данных об экспонатах
for i in range(n):
    b = [0, 0]
    a = input('Вес и цена: ').split()
    b[0] = int(a[0])
    b[1] = int(a[1])
    arr.append(b)
    arr[i].append(arr[i][1] / arr[i][0])
print(arr)

arr1 = sort_rub_kg(arr)
arr2 = sort_max_rub(arr)
summ = 0

for i in range(m):
    summ1 = 0
    summ2 = 0
    print('Заход ' + str(i + 1))
    temp_arr = arr
    temp_k = k
    for j in temp_arr:
        if j[0] <= temp_k:
            print(j)
            temp_k -= j[0]
            arr.pop(arr.index(j))
            summ += j[1]

print(summ)

