import numpy as np
import math
import matplotlib.pyplot as plt


# y'' = -y --> f(x, y, y') = y
# y(0)=1, y'(0)=0

def f(x, y, dy, d2y, d3y, d4y):
    return 2 * d2y - y + dy + d3y - d4y ** 3

x0 = 0
y0 = (1, 0, 2, -1, 4)

def solucao(x):
    return np.cos(x)

h = 2 ** (-3) # tamanho do passo
xn = 0.5 * np.pi
n = math.ceil((xn - x0) / h)

def euler_2nd(f, x0, y0, h, n):
    x = {k: x0 + k * h for k in range(n + 1)}
    u, v = {}, {}
    u[0], v[0] = y0
    for k in range(n): # para k variando de 0 até n - 1
        u[k + 1] = u[k] + v[k] * h
        v[k + 1] = v[k] + f(x[k], u[k], v[k]) * h
    return tuple(x.values()), tuple(u.values())


def euler_nth(f, x0, y0, h, n):
    x = {k: x0 + k * h for k in range(n + 1)}
    ordem = len(y0) # ordem da edo
    u = {k: {0: y0[k]} for k in range(ordem)} # u[0], u[1], u[2],..., u[ordem - 1]
    for k in range(n): # para k variando de 0 até n - 1
        for m in range(ordem - 1):
            u[m][k + 1] = u[m][k] + u[m + 1][k] * h
        u[ordem - 1][k + 1] = u[ordem - 1][k] + f(x[k], *[var[k] for var in u.values()]) * h
    return tuple(x.values()), tuple(u[0].values())

# x, y = euler_2nd(f, x0, y0, h, n)
x2, y2 = euler_nth(f, x0, y0, h, n)

t = np.linspace(x0, n * h, 100)

# plt.plot(t, solucao(t))
# plt.scatter(x, y, label='Euler')
plt.scatter(x2, y2, label='Euler generalizado')
plt.legend()
plt.show()
