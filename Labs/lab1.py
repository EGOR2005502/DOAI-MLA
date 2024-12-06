import numpy as np

x,y,z=float(input('Введите переменные')),float(input('Введите переменные')),float(input('Введите переменные'))
print(np.round((np.sqrt(10*((x)**1/3)+x**(y+2))*((np.arcsin(np.radians(z)))**2-abs(x))),2))
