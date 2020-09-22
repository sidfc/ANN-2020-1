import matplotlib.pyplot as plt
import numpy as np
# y' = 2 * y + x + 1, y(x0) = y0
# possui única solução pelo EXU

x0, y0 = 1, 2
h = 0.125 # tamanho do passo
n = 100

def f(x, y):
    return 2 * y + x + 1

def solucao_do_pvi(x):
    return (1/4) * (-2 * x + 13 * np.exp(2 * x - 2) - 3)

def euler(f, x0, y0, h, n):
    x = {0: x0}
    y = {0: y0}
    for i in range(1, n):
        x[i] = x0 + i * h # <- listando os pontos na partição
        y[i] = y[i - 1] + f(x[i - 1], y[i - 1]) * h # <- fórmula do método
    return x, y

def heun(f, x0, y0, h, n):
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + h, y[k] + m1 * h)
        y[k + 1] = y[k] + (h / 2) * (m1 + m2) # <- fórmula do método de Heun
    return x, y

def euler_mid(f, x0, y0, h, n):
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + h / 2, y[k] + m1 * h / 2)
        y[k + 1] = y[k] + h * m2 # <- fórmula do método de Euler do ponto médio
    return x, y

def ralston(f, x0, y0, h, n):
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + h, y[k] + m1 * h)
        y[k + 1] = y[k] + (h / 3) * (1 * m1 + 2 * m2) # <- fórmula do método de Ralston
    return x, y

def rk2(f, x0, y0,c2, h, n):
    # c1 + c2 = 1 --> c1 = 1 - c2, c2 > 0
    c1 = 1 - c2
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + h, y[k] + m1 * h)
        y[k + 1] = y[k] + h * (c1 * m1 + c2 * m2) # <- fórmula do método de RK2
    return x, y

def rk4(f, x0, y0, h, n):
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + h / 2, y[k] + m1 * h / 2)
        m3 = f(x[k] + h / 2, y[k] + m2 * h / 2)
        m4 = f(x[k] + h, y[k] + m3 * h)
        y[k + 1] = y[k] + (h / 6) * (m1 + 2 * m2 + 2 * m3 + m4) # <- fórmula do método de Runge-Kutta
    return x, y

metodos = [euler, heun, euler_mid, ralston, rk4]
names = ['Euler', 'Heun', 'Euler médio', 'Ralston', 'Runge-Kutta 4']

t = np.linspace(x0, x0 + n * h, 100)

for name, metodo in zip(names, metodos):
    xs, ys = metodo(f, x0, y0, h, n)
    x = list(xs.values())
    y = list(ys.values())

    plt.scatter(x, y, label=name)
    plt.plot(t, solucao_do_pvi(t))

plt.legend()
plt.show()
