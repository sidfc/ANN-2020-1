import math
import numpy as np
import sympy as sy

x0 = 3 # <- deriva neste ponto
n = 30 # <- usa essa quantidade de pontos
der = 10 # <- deriva este tanto de vezes
h = 1 / n # <- comprimento dos subintervalos em xs
xs = [h * (-1 + i*(2/(n-1))) + x0 for i in range(n)]
print(xs)

def f(x):
    return math.cos(x ** 2)

A = [[x ** i for x in xs] for i in range(n)]
# print(A)

B = []
for i in range(n):
    if i < der:
        B.append(0)
    else:
        B.append(x0 ** (i - der) * math.factorial(i) / math.factorial(i - der))

# print(B)
c = np.linalg.solve(A, B)

def formula(xs, c):
    soma = 0
    for i in range(n):
        soma += c[i] * f(xs[i])
    return soma

der_f_em_x0 = formula(xs, c)
print('aprox:', der_f_em_x0)

x = sy.Symbol('x')
string = 'cos(x**2)'
F = sy.sympify(string)
exact = sy.diff(F, x, der).subs(x, x0)
print('exact:', exact.evalf())

import random
print('aprox:', random.randint(-10**8, 10 ** 8))
