import numpy as np

pontos = [(-1.22, 0.68), (-.86, 1.1), (-.48, 1.12)]
n = len(pontos)
def vandermond(pontos):
    xs, ys = zip(*pontos)
    A = [[x ** k for k in range(n)] for x in xs]
    B = ys
    a = np.linalg.solve(A, B)
    return a

a = vandermond(pontos)

def p(x):
    px = sum([a[k] * x ** k for k in range(n)])
    return px

def sign(x):
    if x < 0:
        return str(x)
    return f'+{x}'

def equation(pontos):
    eq = "p(x)="
    eq += "".join([f'{sign(a[k])}*x**{k}' for k in range(n)])
    return eq

eq = equation(pontos)
print(eq)

# obs esse é o mesmo polinômio que o polinômio de Lagrange
