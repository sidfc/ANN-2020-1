# uma função qualquer
def f(x):
    return x ** 5 - 8 * x - 2

# derivada de f
def df(x):
    return 5 * x ** 4 - 8

x0 = 2
n = 10
itr = {}
itr[0] = x0
for i in range(1, n):
    itr[i] = x0 - f(x0) / df(x0)
    x0 = itr[i]

for k, v in itr.items():
    print(k, v, abs(v - 1.7392201937014509))
