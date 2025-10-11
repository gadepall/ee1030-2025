// main.c

#include <stdio.h>

// Cross product: result = u x v
void cross_product(const double u[3], const double v[3], double result[3]) {
    result[0] = u[1]*v[2] - u[2]*v[1];
    result[1] = u[2]*v[0] - u[0]*v[2];
    result[2] = u[0]*v[1] - u[1]*v[0];
}

// Dot product: returns u . v
double dot_product(const double u[3], const double v[3]) {
    return u[0]*v[0] + u[1]*v[1] + u[2]*v[2];
}

// Scalar triple product: (a x c) . b
double scalar_triple_product(const double a[3], const double b[3], const double c[3]) {
    double cross[3];
    cross_product(a, c, cross);
    return dot_product(cross, b);
}

