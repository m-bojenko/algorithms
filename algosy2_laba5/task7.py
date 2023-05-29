def propusk(mas):
    """ функция для поиска наименьшего пропущенного числа """

    pros = set()
    for i in mas:
        if i in pros:
            pros.remove(i)
        if i + 2 not in pros:
            pros.add(i+1)
    return min(pros)


print(propusk([6, 2, 4, 1, 11, 8, 3]))
