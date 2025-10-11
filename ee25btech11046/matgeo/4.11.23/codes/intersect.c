#include <stdio.h>
double dot(double *a, double *b) {
    double sum = 0;
    for (int i=0; i<3; i++) {
        sum += a[i]*b[i];
    }
    return sum;
}
void function(double *p, double *m, double *n, double c, double *x) {
    for (int i=0; i<3; i++) {
        x[i] = p[i] + ((c-dot(n, p))/(dot(n, m)))*m[i];
    }
}
