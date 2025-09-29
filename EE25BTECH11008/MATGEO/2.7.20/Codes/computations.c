#include <math.h>

// Function 1: find diagonals from A and B
void diagonals(double A[3], double B[3], double d1[3], double d2[3]) {
    d1[0] = A[0] - B[0];
    d1[1] = A[1] - B[1];
    d1[2] = A[2] - B[2];

    d2[0] = A[0] + B[0];
    d2[1] = A[1] + B[1];
    d2[2] = A[2] + B[2];
}

// Function 2: dot product
double dot(double a[3], double b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// Function 3: unit vector
void unit(double v[3], double u[3]) {
    double mag = sqrt(dot(v, v));
    u[0] = v[0]/mag;
    u[1] = v[1]/mag;
    u[2] = v[2]/mag;
}

// Function 4: cross magnitude via dot relation
double cross_via_dot(double a[3], double b[3]) {
    double mag_a2 = dot(a, a);
    double mag_b2 = dot(b, b);
    double dot_ab = dot(a, b);
    return sqrt(mag_a2 * mag_b2 - dot_ab * dot_ab);
}
