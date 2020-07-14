import math

exact = 0.746824132812427025#399467436131853005354499686812606329027654498958605327561772831497848429822901920' # exp(-x^2)
# exact = 0.9045242379002720#81474788366832557145807991820595501739598320037451079592676477307938916761063727488' # cos(x^2)

a, b = 0, 1
def f(x):
    return math.exp(-x ** 2)

def trapezo(f, h, xs):
    last = len(xs) - 1
    soma = f(xs[0]) + f(xs[last])
    soma += 2 * sum([f(x) for i, x in enumerate(xs) if i not in [0, last]])
    return (h / 2) * soma

def simpson(f, h, xs):
    last = len(xs) - 1
    soma = f(xs[0]) + f(xs[last])
    soma += 2 * sum([f(xs[i]) for i in range(2, last, 2)])
    soma += 4 * sum([f(xs[i]) for i in range(1, last, 2)])
    return (h / 3) * soma

for n in range(10):
    h = (b - a) / 2 ** n
    xs = [a + k * h for k in range(2 ** n + 1)]
    aprox = simpson(f, h, xs)
    print('qtde:', 2 ** n, 'aprox:', aprox, 'erro:', abs(exact - aprox))
