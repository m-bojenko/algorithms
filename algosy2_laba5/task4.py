count = 0


def stairs(mas, add, end, start=0):
    mas.append(add)
    start += add
    if start == end:
        global count
        count += 1
        mas.pop(0)
        print(mas)
    elif end > start:
        new_mas = []
        for i in range(len(mas)):
            new_mas.append(mas[i])
        stairs(new_mas, 1, end, start)
        new_mas = []
        for i in range(len(mas)):
            new_mas.append(mas[i])
        stairs(new_mas, 2, end, start)
        new_mas = []
        for i in range(len(mas)):
            new_mas.append(mas[i])
        stairs(new_mas, 3, end, start)


arr = []
stairs(arr, 0, 10)
print(count)
