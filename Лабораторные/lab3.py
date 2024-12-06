import math as m
import numpy as np
x1 = 2
xn = 5
dx = 0.5
a = 1.5
b = 4.8


def fx(x):
    return a*((b/x)-((np.log(a*x))/b*b))


n = x1
print('цикл while')
while not n >= xn:
    n += dx
    print('x= ', round(n, 3), 'f(x) = ', round(fx(n), 7))
print('цикл for')
for i in np.arange(x1, xn, dx):
    print('x= ', round(i, 3), 'f(x) = ', round(fx(i), 7))
