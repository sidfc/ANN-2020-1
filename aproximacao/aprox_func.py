import math
import random as r
import matplotlib.pyplot as plt
import numpy as np

a, b = 0, 3
n = 100
xs = [a + (b - a) * r.random() for _ in range(n)]
xs.sort()
def data(x):
    erro = r.random() / 1000
    val = 2 * x ** 3.2 + erro
    return val
ys = [data(x) for x in xs]

# x --> x_til = ln(x)
xs_new = [math.log(x) for x in xs]
# y --> y_til = ln(y)
ys_new = [math.log(y) for y in ys]
pontos = list(zip(xs_new, ys_new))

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

# y_til = a_0 + a_1 + x_til
coefs = min_q(pontos) # [a0, a1]
# def p(x): # <-- a melhor reta
#     # a0 + ai * x
#     return sum(c * x ** i for i, c in enumerate(coefs))

a_ = math.exp(coefs[0])
b_ = coefs[1]
print(a_, b_)

def expo(x): # y = a * exp(b * x) # é a melhor função exponencial
    return a_ * math.exp(b_ * x)

def poten(x): # y = a * x ** b # é a melhor função potência
    # sensível demais ;(
    return a_ * x ** b_

plt.scatter(xs, ys)
h = (b - a) / n

t = [a + i * h for i in range(n)]
yt = [poten(x) for x in t]

plt.plot(t, yt, 'r')
plt.show()
