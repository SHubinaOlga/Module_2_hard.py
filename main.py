def pass_(number):
    num_ = ' '
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                num_ += str(i) + str(j)
    return num_


print('Введите число: ')
print('Ваш пароль: ', pass_(int(input())))