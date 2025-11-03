#include <stdio.h>

double find_k() {
    double a = 6, b = 37, c; 
    double k;

    c = a;

    k = 2 - a;
    return k;
}

int main() {
    double k = find_k();
    printf("The value of k = %.2lf\n", k);
    return 0;
}
