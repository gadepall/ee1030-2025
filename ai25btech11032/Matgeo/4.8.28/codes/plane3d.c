#include <stdio.h>
#include <math.h>

// dot product
double dot(const double *a, const double *b, int n) {
    double s = 0.0;
    for (int i = 0; i < n; i++) s += a[i] * b[i];
    return s;
}

// compute n = n1 + k n2
void compute_n(const double *n1, const double *n2, double k, double *res, int n) {
    for (int i = 0; i < n; i++) res[i] = n1[i] + k*n2[i];
}

// compute constant C = c1 + k c2
double compute_C(double c1, double c2, double k) {
    return c1 + k*c2;
}

// compute k = -(ex·n1)/(ex·n2)
double find_k(const double *ex, const double *n1, const double *n2, int n) {
    double num = dot(ex,n1,n);
    double den = dot(ex,n2,n);
    return -num/den;
}

// norm of vector
double norm(const double *a, int n) {
    return sqrt(dot(a,a,n));
}

// distance = |C| / ||n||
double plane_distance(const double *n, double C, int nlen) {
    return fabs(C)/norm(n,nlen);
}

// foot of perpendicular from origin to plane: (C/||n||^2) * n
void foot_point(const double *n, double C, double *res, int nlen) {
    double factor = C/dot(n,n,nlen);
    for (int i = 0; i < nlen; i++) res[i] = factor*n[i];
}

