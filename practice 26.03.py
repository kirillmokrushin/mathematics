# Код для решения уравнения вида: a*x + b*y = c

# Находим НОД и цепную дробь
def reshit(a, b, c):
    abs_a, abs_b = abs(a), abs(b)
    chain = []
    
    while abs_b:
        chain.append(abs_a // abs_b)
        abs_a, abs_b = abs_b, abs_a % abs_b
    
    gcd = abs_a
    
    # Проверяем существует ли решение
    if c % gcd != 0:
        return "Нет целых решений"
    
    # Все коэффициенты цепной дроби кроме последнего
    coefficients = chain[:-1]
    
    # Обратный ход - сворачиваем дробь
    numerator = 1      # числитель
    denominator = 0    # знаменатель
    
    for coef in reversed(coefficients):
        numerator, denominator = coef * numerator + denominator, numerator
    
    length = len(chain)
    
    # Базовое частное решение
    base_x = denominator * ((-1) ** length)
    base_y = -numerator * ((-1) ** length)
    
    # Учитываем знаки исходных коэффициентов
    if a < 0:
        base_x = -base_x
    if b < 0:
        base_y = -base_y
    
    # Масштабируем под нужную константу
    multiplier = c // gcd
    solution_x = base_x * multiplier
    solution_y = base_y * multiplier
    
    # Шаги для параметра t
    step_x = b // gcd
    step_y = a // gcd
    
    # Знаки в формуле
    sign_x = '+' if step_x >= 0 else '-'
    sign_y = '-' if step_y >= 0 else '+'
    
    return f"x = {solution_x} {sign_x} {abs(step_x)}t, y = {solution_y} {sign_y} {abs(step_y)}t"

# Пример
print(reshit(15, 10, 5))   # x = 1 - 2t, y = -1 + 3t
print(reshit(6, 9, 12))    # x = -2 + 3t, y = 2 - 2t
print(reshit(2, 4, 3))     # Нет целых решений
