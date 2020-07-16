# uma função qualquer
def f(x):
    return x ** 5 - 8 * x - 2

n = 11
x0, x1 = [1, 2]
itr = {}
itr[0] = x0
itr[1] = x1

a, b = x0, x1
for i in range(n):
    try:
        xn = (a * f(b) - b * f(a)) / (f(b) - f(a)) # a - f(a) / ((f(b) - f(a))/ (b - a))
    except:
        raise ValueError(f"Divisão por zero para {a}, {b} na iteração {i}")
    itr[i + 2] = xn
    a, b = b, xn

for k, v in itr.items():
    print(k, v, abs(v - 1.7392201937014509))

