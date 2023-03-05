def crc32(line, kind='1'):
    ieee = '100000100110000010001110110110111'
    crc_3121 = '11110111011100010010100011001100'
    c = '100011110110111000110111101000001'
    k = '101110100000110111000110011010111'
    q = '110000001010000010100000110101011'
    test = '11001'

    poli = ''
    if kind == '1':
        poli = ieee
    elif kind == '2':
        poli = c
    elif kind == '3':
        poli = k
    elif kind == '4':
        poli = q
    elif kind == '5':
        poli = test

    # new_line = line + '0010'
    # new_line = line + crc_3121
    new_line = line
    for i in range(32):
        new_line += '0'

    x = ''
    while len(new_line) + len(x) >= len(poli):
        while len(x) < len(poli):
            x += new_line[0]
            new_line = new_line[1:]

        xor = int(x, 2) ^ int(poli, 2)
        x = bin(xor)[2:]

    return x + new_line


def main():
    line = input('Введите текст: ')
    new_line = ''
    if line.count('1') + line.count('0') == len(line):
        print(f'Захешированный текст: {crc32(new_line)}')
    else:
        for i in range(len(line)):
            new_line += bin(ord(line[i]))[2:]
        print(f'Захешированный текст: {crc32(new_line)}')


main()

# print(crc32('10011101', '5'))

# a = '1001'
# b = '0011'
# c = int(a, 2) ^ int(b, 2)
# print(bin(c)[2:])

