import matplotlib.pyplot as plt
import numpy as np
# y' = 2 * y + x + 1

x0, y0 = 1, 2
h = 2 ** (-5) # tamanho do passo
n = 100

def f(x, y):
    return 2 * y + x + 1

def s(x):
    return (1/4) * (-2 * x + 13 * np.exp(2 * x - 2) - 3)

x = {0: x0}
y = {0: y0}

for i in range(1, n):
    x[i] = x0 + i * h # <- listando os pontos na partição
    y[i] = y[i - 1] + f(x[i - 1], y[i - 1]) * h # <- fórmula do método



x = [v for _, v in x.items()]
y = [v for _, v in y.items()]

print(x)
print(y)

t = np.linspace(x0, x0 + n * h, 100)
plt.scatter(x, y)
plt.plot(t, s(t))
plt.show()
