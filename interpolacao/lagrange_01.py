# Polinômio interpolador

"""
- Um polinômio p(x), de grau n, é o polinômio interpolador
de uma lista contendo n+1 de pontos
pontos = [(x0,y0), (x1,y1), (x2,y2), ..., (xn, yn)]
se p(xk) = yk, para todo k=0,1,2,...,n.

- Se os pontos da lista acima pertencem ao gráfico de uma
função f, i.e., se yk=f(xk), para todo k=0,1,2,...,n, dizemos
que o polinômio p(x) interpola a função f no pontos da lista.

- Útil para estimar valores fora da lista dada de pontos
- Útil para aproximar funções (nem sempre)
"""

# Ex1
# lista = [(1,2)]
# # p(1)=2, p(x)==2, tem grau zero.
# def p(x):
#     return 2

lista = [(2, -1), (5, 4)]
# p(2) = -1 e p(5) = 4, tem grau 1

# a, b = 1, 7
# # f(a) = 0 e f(b) = 1
# def f(x):
#     return (x - a) / (b - a)

# L0 e L1, uma para cada ponto

# L0(2) = 1 e L0(5) = 0
# def L0(x):
#     return (x - 5) / (2 - 5)

# # L1(5) = 1 e L1(2) = 0
# def L1(x):
#     return (x - 2) / (5 - 2)

# def p(x):
#     return -1 * L0(x) + 4 * L1(x)

lista = [(2,-2), (3, 4), (5, -1)]
# L0(2)=1, L0(3)=0, L0(5)=0
def L0(x):
    return ((x - 3) * (x - 5)) / ((2 - 3) * (2 - 5))

# L1(2)=0, L1(3)=1, L1(5)=0
def L1(x):
    return ((x - 2)*(x - 5)) / ((3 - 2)*(3 - 5))

# L2(2)=0, L2(3)=0, L2(5)=1
def L2(x):
    return ((x - 2)*(x - 3)) / ((5 - 2)*(5 - 3))

def p(x):
    return -2 * L0(x) + 4 * L1(x) - 1 * L2(x)

print(p(2), p(3), p(5))


