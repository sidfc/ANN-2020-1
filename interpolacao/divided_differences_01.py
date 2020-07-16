pontos = [(1, 2), (2, 5), (3, -1), (4, 2), (3.1, 3), (1.2, 8)]
xs, ys = zip(*pontos)
n = len(pontos)

# auxiliares
def prod(lista):
    p = 1
    for i in lista:
        p *= i
    return p

def sign(x):
    if x < 0:
        return str(x)
    return f'+{x}'

# algoritmo
def tabela(pontos):
    Y = {}
    Y[0] = {k: v for k, v in enumerate(ys)}
    for j in range(1, n):
        Y[j] = {}
        for i in range(n - j):
            Y[j][i] = (Y[j - 1][i + 1] - Y[j - 1][i]) / (xs[j + i] - xs[i])
    return Y

t = tabela(pontos)
a = [v[0] for k, v in t.items()]

def p(x):
    soma = 0
    for k in range(n):
        termo_k = prod([(x - xi) for i, xi in enumerate(xs) if i < k])
        soma += a[k] * termo_k
    return soma

def eq(coefs):
    equation = ""
    for k in range(n):
        termo_k = "*".join([f'(x{sign(-xi)})' for i, xi in enumerate(xs) if i < k])
        if k == 0:
            equation += str(a[k])
        else:
            equation += f'{sign(a[k])}*' + termo_k
    return equation

poly = eq(a)
print(poly)

# Método das diferenças divididas (de Newton)

import matplotlib.pyplot as plt
import numpy as np

def poly_f(x):
    return eval(poly)

a, b = min(xs) - 0.5, max(xs) + 0.5
t = np.arange(a, b, 0.01)
plt.scatter(xs, ys)
plt.plot(t, poly_f(t), color="red", label="polinômio interpolador")
plt.show()
