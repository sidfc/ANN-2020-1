n = 5 # ordem do erro
x0 = 2
h = .5
p = 2

def f(x):
    return x ** x

# def F1(h):
#     return (f(x0 + h) - f(x0)) / h

def F1(h):
    return (f(x0 - h) - 2 * f(x0) + f(x0 + h)) / h ** 2

print('aprox2:', F1(h))

def Fk(h, n, p):
    # I'm recursive :)
    if n == 1:
        return F1(h)
    n -= 1
    return (2 ** (n * p) * Fk(h/2, n, p) - Fk(h, n, p)) / (2 ** (n * p) - 1)

print(f'aprox{n}:', Fk(h, n, p))

import sympy as sy

x = sy.Symbol('x')
f = sy.sympify('x ** x')
df = sy.diff(f, x, 2).subs(x, x0).evalf()
print('exact:', df)
