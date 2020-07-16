# posição pode ser mais lento que o método da bisseção

# uma função qualquer
def f(x):
    return x ** 5 - 8 * x - 2

n = 30
a, b = [1, 2]
for i in range(n):
    xn = (a * f(b) - b * f(a)) / (f(b) - f(a))
    if f(xn) == 0:
        print('A raiz é:', xn)
    elif f(a) * f(xn) < 0:
        b = xn
    else:
        a = xn
    print(i, xn, abs(xn - 1.7392201937014509))
