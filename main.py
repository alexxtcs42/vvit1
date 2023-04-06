try:
    [a, b, c] = [float(e) for e in input('Введите коэффициенты a, b, c через пробел: ').split()]
    d = b * b - 4 * a * c
    if a == 0:
        print('Уравнение не квадратное')
    elif d == 0:
        print(f'x = {(-1 * b) / (2 * a)}')
    elif d > 0:
        print(f'x1 = {(-1 * b - d ** 0.5) / (2 * a)}')
        print(f'x2 = {(-1 * b + d ** 0.5) / (2 * a)}')
    else:
        print('Уравнение не имеет действительных корней')
except Exception:
    print('Неверные входные данные')
