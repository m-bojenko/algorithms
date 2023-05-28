#Бинарный поиск
def f(arr,x):
    l = 0
    r = len(arr)
    if arr[r-1] < x or arr[l] > x: return -1
    while r > l:
        mid = (l+r)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid+1
        else:
            r = mid
    return -1
#Матрица
matrix = [
    [1,2,3],
    [2,3,4],
    [3,4,5]]

x = int(input('Искомый элемент: '))
arr = []
for i in range(len(matrix)):
    arr += [(i,f(matrix[i],x))]
newarr = []
for i in arr:
    if i[1] != -1:
        newarr += [i]
print(newarr)
