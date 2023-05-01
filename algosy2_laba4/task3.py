import random

mas = []
n = int(input('Введите длину массива: '))

for i in range(n):
    mas.append(random.randint(-100, 100))

print(mas)

series = []
k = 1
for i in range(n-1):
    if mas[i+1] > mas[i]:
        k += 1
    else:
        series.append(k)
        k = 1

print(max(series))
