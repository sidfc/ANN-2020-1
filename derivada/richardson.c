// #include <math.h>
#include <stdio.h>

// quando eu descobrir como implementar hash tables no C eu termino este algoritmo

double Fk(double h, double k) {
    double F1h[] = {1.423425, 1.547362, 1.553842, 1.559343};
    if (k == 1) {
        return F1h[]; // <-- preciso de uma hash table aqui
    }
    k -= 1;
    return (pow(2,1 * k) * Fk(h / 2, k) - Fk(h, k)) / (pow(2, 1 * k) - 1);
}

int main() {
    printf("aprox: %10.16lf \t erro: %10.16lf\n", r, mod(exact - r));
    return 0;
}