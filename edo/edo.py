import matplotlib.pyplot as plt
import numpy as np
# y' = 2 * y + x + 1, y(x0) = y0
# possui única solução pelo EXU

x0, y0 = 1, 2
h = 0.125 # tamanho do passo
n = 50

def f(x, y):
    return 2 * y + x + 1

def s(x):
    return (1/4) * (-2 * x + 13 * np.exp(2 * x - 2) - 3)

def euler(f, x0, y0, h):
    x = {0: x0}
    y = {0: y0}
    for i in range(1, n):
        x[i] = x0 + i * h # <- listando os pontos na partição
        y[i] = y[i - 1] + f(x[i - 1], y[i - 1]) * h # <- fórmula do método
    return x, y

def heun(f, x0, y0, h):
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + h, y[k] + m1 * h)
        y[k + 1] = y[k] + (h / 2) * (m1 + m2) # <- fórmula do método de Heun
    return x, y

xs, ys = euler(f, x0, y0, h)
x = [v for _, v in xs.items()]
y = [v for _, v in ys.items()]

hxs, hys = heun(f, x0, y0, h)
hx = [v for _, v in hxs.items()]
hy = [v for _, v in hys.items()]

t = np.linspace(x0, x0 + n * h, 100)

plt.scatter(x, y, label="Euler")
plt.scatter(hx, hy, label="Heun")
plt.plot(t, s(t))
plt.legend()
plt.show()
