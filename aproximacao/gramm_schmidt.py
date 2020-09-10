import numpy as np
import matplotlib.pyplot as plt

def simpson(f, a, b, intervalos):
    h = (b - a) / intervalos
    soma = f(a) + f(b)
    soma += 2 * sum(map(f, [a + i * h for i in range(2, intervalos, 2)]))
    soma += 4 * sum(map(f, [a + i * h for i in range(1, intervalos, 2)]))
    return (h / 3) * soma


def gram_schimdt(fs, a, b, intervalos=100):
    ortogonais = [fs[0]]
    for f in fs[1:]:
        prox_fun_ort = f # fn - a1*f1 - a2*f2 - ... - a(n-1)*f(n-1)
        for fun in ortogonais:
            num = simpson(lambda x : eval(f) * eval(fun), a, b, intervalos) # <f, fk> = int_a^b(f*fk)dx
            den = simpson(lambda x : eval(fun) * eval(fun), a, b, intervalos) # <fk, fk> = int_a^b(fk*fk)dx
            coef = num / den
            if abs(coef) > 10 ** (-10):
                prox_fun_ort += f'{-coef:+.6f} * {fun}'
        ortogonais.append(prox_fun_ort)
    return ortogonais

n = 5
fs = ['1'] + [f'x**{i}' for i in range(1, n)]
a, b = -1, 1

r = gram_schimdt(fs, a, b)

print(fs)
print('Legendre:', r)

t = np.linspace(a, b, 100)
for f in r:
    def fi(x): return eval(f) / np.sqrt(simpson(lambda x : eval(f) * eval(f), a, b, 1000)) # (<f, f>)^(0.5)
    fit = fit = [fi(x) for x in t]
    plt.plot(t, fit, label=f'$f(x)={f}$')
# plt.legend()
plt.show()

