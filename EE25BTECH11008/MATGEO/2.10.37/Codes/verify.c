#include <stdio.h>

// compute cross product: r = a × b
void cross(const double a[3], const double b[3], double r[3]) {
    r[0] = a[1]*b[2] - a[2]*b[1];
    r[1] = a[2]*b[0] - a[0]*b[2];
    r[2] = a[0]*b[1] - a[1]*b[0];
}

// dot product
double dot(const double a[3], const double b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// main function to compute (a+b+c)·[(a+b)×(a+c)]
double expr_value(double a[3], double b[3], double c[3]) {
    double ab[3], ac[3], sum[3], crossp[3];
    for (int i=0; i<3; ++i) {
        ab[i] = a[i] + b[i];
        ac[i] = a[i] + c[i];
        sum[i] = a[i] + b[i] + c[i];
    }
    cross(ab, ac, crossp);
    return dot(sum, crossp);
}
