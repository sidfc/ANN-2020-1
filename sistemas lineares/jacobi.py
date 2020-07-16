E = [[9,1,1,3,6], [2,7,2,1,3], [1,2,6,1, 11], [1,1,1,19,0]] # matrix estendida do sistema
# 4x+y+z=6 --> x = (6 - y - z) / 4
# 2x+5y+2z=3 --> y = (3 - 2x - 2z) / 5
# x+2y+4z=11 --> z = (11 - x - 2y) / 4

def test(matrix, vec):
    err = []
    for row in matrix:
        prod = abs(sum([col * vec for col, vec in zip(row[:-1], vec)]) - row[-1])
        err.append(prod)
    return err

n  = 50
itr = {}
chute = [0,0,0,1]
for i in range(n):
    xn = []
    for j, row in enumerate(E):
        coefs = [-el for k, el in enumerate(row[:-1]) if k != j]
        vec = [c for k, c in enumerate(chute) if k != j]
        subs = (row[-1] + sum([c * v for c, v in zip(coefs, vec)])) / row[j]
        xn.append(subs)
    print(xn, test(E, xn))
    chute = xn

