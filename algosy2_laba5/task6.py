def exp_filter(mas, k):
    """ функция, описывающая экспоненциальный фильтр """

    result = [mas[0]]
    for i in range(1, len(mas)):
        next_num = k * mas[i] + result[i-1] * (1 - k)
        result.append(next_num)
    return result


print(exp_filter([1, 2, 3, 2, 1], 0.5))
