import math
import matplotlib.pyplot as plt
import numpy as np


def simpson(f, a, b, intvals):
    h = (b - a) / intvals
    # xs = [a + i * h for i in range(intvals + 1)]
    # last = len(xs) - 1
    soma = f(a) + f(b)
    soma += 2 * sum(map(f, [a + i * h for i in range(2, intvals, 2)]))
    soma += 4 * sum(map(f, [a + i * h for i in range(1, intvals, 2)]))
    return (h / 3) * soma

def coefs(f, a, b, n, intvals=100):
    ans, bns = [], []
    c = simpson(f, a, b, intvals) / (2 * math.pi) # (1/2pi)*int_a^b f(x)dx
    for i in range(1, n):
        def fi(x):
            return f(x) * math.cos(i * x)
        ans.append(simpson(fi, a, b, intvals) / math.pi) # a_i = (1/pi) * int_a^bf(x)*cos(i*x)dx
        def fi(x):
            return f(x) * math.sin(i * x)
        bns.append(simpson(fi, a, b, intvals) / math.pi) # b_i = (1/pi) * int_a^bf(x)*sin(i*x)dx
    return c, ans, bns

def f(x):
    return math.cos(x ** 2) + x ** 2

a, b = -math.pi, math.pi
c, ans, bns = coefs(f, a, b, 50)

# def sign(x):
#     if x < 0:
#         return str(x)
#     return f'+{x}'

def eq(c, ans, bns):
    equation = f"{c} "
    n = len(ans)
    for i in range(n):
        equation += f" {ans[i]:+} * math.cos({i + 1} * x)"
        equation += f" {bns[i]:+} * math.sin({i + 1} * x)"
    return equation

eq_string = eq(c, ans, bns)
print(eq_string)
def fourier(x):
    return eval(eq_string)

t = np.arange(a, b, 0.01)
f_t = [f(x) for x in t]
fourier_t = [fourier(x) for x in t]

plt.plot(t, f_t, label="função $f(x)=\\cos(x^2)+x^2$")
plt.plot(t, fourier_t, label="serie de fourier")
plt.legend()
plt.show()
