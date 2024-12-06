import math as m


b = True
a = 0
x, y = float(input('x=')), float(input('y='))
hp1 = x/y > 0
hp2 = x/y < 0

def fx1(y):
    return m.sinh(m.radians(y))

def fx2(y):
    return x**m.e**x

def fx3(x):
    return x**y

while b:
    gh = input('f1 == 1, f2 == 2, f3 == 3: ')
    if gh == '1':
        a = fx1(y)
        b = False
    elif gh == '2':
        a = fx2(y)
        b = False
    elif gh == '3':
        a = fx3(x)
        b = False
    else:
        print('Invalid input')
        gh = ''

if hp1:
    c = m.e**(a-abs(y))
elif hp2:
    c = (abs(a+y))**(1/3)
else:
    c = 2*a**2
print('c=', c)
