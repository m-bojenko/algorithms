def f(a, b=1):
    if a > b:
        return 0
    elif a == b:
        return 1
    elif a < b:
        return f(a+3, b) + f(a+2, b) + f(a+1, b)


inp = int(input('Введите номер ступеньки, до которой нужно добраться (N >= 1): '))
print(f(0, inp))
