# uma função qualquer
def f(x):
    return x ** 5 - 8 * x - 2

# método da bisseção
a, b = [0, 2]
n = 50 # número de iterações
for i in range(n):
    m = (a + b) / 2
    if f(m) == 0:
        print('A raiz é:', m)
    elif f(a) * f(m) < 0: # teorema de Bolzano
        b = m
    else:
        a = m
    print(m, f(m))
