#include <math.h>
#include <stdio.h>

// exact = 0.7468241328124270253994674361318530053544996868126063290276544989586053275617728314978484298229019197;
// integral exp(-x^2) x=0..1

// escrever a regra dos trapézios para a função f: F1
double F1(double h) {
    // aqui você pode modificar
    double a = 0, b = 1;
    double n = (b - a) / h;
    double f(double x) {
        return exp(- x * x);
    }
    // não modifique
    double aprox = 0.0;
    for (int i = 1; i < n; i++) {
        double xi = a + h * i;
        aprox += f(xi);
    }
    return (h / 2) * (f(a) + 2 * aprox + f(b));
}

double mod(double x) {
    if (x < 0)
        return -x;
    return x;
}
//formula de Romberg: Fk

double Fk(double h, double k) {
    if (k == 1)
        return F1(h);
    k -= 1;
    return (pow(2, 2 * k) * Fk(h / 2, k) - Fk(h, k)) / (pow(2, 2 * k) - 1);
}

int main() {
    double h = 1 / pow(2, 2);
    int k = 4; // com isso o erro será de ordem 2 * (k + 1)
    double t = F1(h);
    double r = Fk(h, k);
    double exact = 0.746824132812;
    printf("aprox: %10.16lf \t erro: %10.16lf\n", t, mod(exact - t));
    printf("aprox: %10.16lf \t erro: %10.16lf\n", r, mod(exact - r));
    return 0;
}