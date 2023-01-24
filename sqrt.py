from math import sqrt

message = ('Добро пожаловать в самую лучшую программу '
           'для вычисления квадратного корня из заданного числа')
print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Вычисляет квадратный корень из вашего числа."""
    if your_number <= 0:
        return
    sqrt_calc = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень '
          f'из введённого вами числа. '
          f'Это будет: {sqrt_calc}')


print(message)
calc(25.5)
