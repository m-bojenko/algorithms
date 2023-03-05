def division(line):
    len_mas = len(line)
    hesh = ''

    for i in line:
        ork = ord(i)
        hesh += str(ork % len_mas) + ' '

    return hesh


def main():
    line = input('Введите строку: ')
    print(f'Захешированная строка: {division(line)}')
    print(str(ord('1')))


main()
