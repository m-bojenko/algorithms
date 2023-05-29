import math

mas = [6, 2, 4, 1, 11, 8, 3]
print(mas)

result = math.inf
mn = min(mas)
mx = max(mas)
b = []
d = dict()
for element in mas:
    d[element] = 1
for i in mas:
    if i != mn and i != mx:
        b.append(i - 1)
        b.append(i + 1)
    elif i == mn:
        b.append(i + 1)
    else:
        b.append(i - 1)
for element in b:
    if element not in d:
        result = min(result, element)

print("Наименьшее пропущенное целое: " + str(result))
