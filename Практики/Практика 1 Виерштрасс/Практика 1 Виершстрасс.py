import numpy as np
import matplotlib.pyplot as plt

def weierstrass_function(x, a, b, n_terms):
    """
    Вычисляет значение функции Вейерштрасса для заданного x.

    Параметры:
    x -- значение аргумента функции
    a -- параметр a функции Вейерштрасса
    b -- параметр b функции Вейерштрасса
    n_terms -- количество членов ряда для суммирования

    Возвращает:
    Значение функции Вейерштрасса в точке x
    """
    result = 0
    for n in range(n_terms):
        result += a**n * np.cos(b**n * np.pi * x)
    return result

# Параметры функции Вейерштрасса
a = 0.5
b = 3
n_terms = 100  # Количество членов ряда для суммирования

# Диапазон значений x
x_values = np.linspace(-2, 2, 1000000)

# Вычисление значений функции Вейерштрасса
y_values = weierstrass_function(x_values, a, b, n_terms)

# Построение графика
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot(x_values, y_values, label=f'Функция Виершстрасса (a={a}, b={b})')
ax.set_title('Функция Виершстрасса')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.grid(True)

plt.show()
