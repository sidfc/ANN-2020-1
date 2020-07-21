def f(x):
    return 6 * x ** 2 - 59 * x + 12

x0 = 2

def f1(x0, h):
    return (f(x0 + h) - f(x0)) / h

def f2(x0, h):
    return (f(x0) - f(x0 - h)) / h

def f3(x0, h):
    return (f(x0 + h) - f(x0 - h)) / (2 * h)

def f4(x0, h):
    return (f(x0 + h) - 2 * f(x0) + f(x0 - h)) / h ** 2

hs = [1, .5, .25, .125, 1/8, 1/16, 1/128, 1/1024, 1 / 2 ** 15]

for h in hs:
    print('aprox:', f4(x0, h))

# import sympy as sy

# x = sy.Symbol('x')
# string = 'x ** x'
# f = sy.sympify(string)
# df = sy.diff(f, x, 2).subs(x, x0)
# print('exact:', df.evalf())
