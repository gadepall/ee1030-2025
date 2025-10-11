#include <stdio.h>
double root(double x) {
    double num = x;
    for (int i = 0; i < 1000; i++) {
        num = (num + x / num)/2;
    }
    return num;
}
double norm(double *a) {
    return root(a[0]*a[0] + a[1]*a[1]);
}
void function(double *a, double *b, double *n1, double *n2, double *p, double *c1, double *c2) {
    n1[0] = - (a[1] / norm(a) + b[1] / norm(b));
    n1[1] = a[0] / norm(a) + b[0] / norm(b);
    n2[0] = - (a[1] / norm(a) - b[1] / norm(b));
    n2[1] = a[0] / norm(a) - b[0] / norm(b);
    *c1 = n1[0] * p[0] + n1[1] * p[1];
    *c2 = n2[0] * p[0] + n2[1] * p[1];
}
