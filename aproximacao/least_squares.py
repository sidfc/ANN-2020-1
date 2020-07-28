import random as r
import matplotlib.pyplot as plt
import numpy as np


# modelo de pontos
a, b = -2, 2
n = 100
xs = [a + (b - a) * r.random() for _ in range(n)]
xs.sort()
num = 10
data_coefs = [r.random() for _ in range(num)]
def data(x):
    # a + b * x + erro
    erro = r.random() / 10
    val = sum(c * x ** i for i, c in enumerate(data_coefs)) + erro
    return val
ys = [data(x) for x in xs]

# método dos mínimos quadrados para retas
def min_q(pontos):
    n = len(pontos)
    sumxk = sum(x for x, _ in pontos)
    sumxk2 = sum(x ** 2 for x, _ in pontos)
    sumyk = sum(y for _, y in pontos)
    sumykxk = sum(x * y for x, y in pontos)
    A = [[n, sumxk], [sumxk,sumxk2]]
    B = [sumyk, sumykxk]
    coefs = np.linalg.solve(A, B)
    return coefs # a0 e a1

# método dos minimos quadrados geral
def least_squares(pontos, k): # se k == 1, então o resultado é o mesmo de min_q(pontos)
    # vamos obter um sistema (k+1)x(k+1)
    n = len(pontos)
    A = {}
    B = []
    for i in range(k + 1):
        A[i] = {}
        for j in range(k + 1):
            if j >= i:
                A[i][j] = sum(x ** (i + j) for x, _ in pontos)
            else:
                A[i][j] = A[j][i]
    A = [[A[i][j] for j in range(k + 1)] for i in range(k + 1)]
    for i in range(k + 1):
        B.append(sum(y * x ** i for x, y in pontos))
    coefs = np.linalg.solve(A, B)
    return coefs


pontos = list(zip(xs, ys))
c = least_squares(pontos, k=15)
print(c)

def fit_poly(x):
    return sum(c * x ** i for i, c in enumerate(c)) # sum c[j] * x ** j, j=0,1,2,...,k

erro = sum((y - fit_poly(x)) ** 2 for x, y in pontos)
t = np.arange(a, b, 0.01)
plt.plot(t, fit_poly(t), 'r', label=f"erro: {erro}")
plt.legend()
plt.scatter(xs, ys)
plt.show()
