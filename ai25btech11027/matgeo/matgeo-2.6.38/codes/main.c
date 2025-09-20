// main.c

#include <stdio.h>

// Cross product of two vectors using pointers
void cross(const double *u, const double *v, double *result) {
    result[0] = u[1]*v[2] - u[2]*v[1];
    result[1] = u[2]*v[0] - u[0]*v[2];
    result[2] = u[0]*v[1] - u[1]*v[0];
}

// Scalar multiplication: result = k * v
void scalar_mult(double k, const double *v, double *result) {
    for (int i = 0; i < 3; i++) {
        *(result + i) = k * (*(v + i));
    }
}

// Vector subtraction: result = u - v
void subtract(const double *u, const double *v, double *result) {
    for (int i = 0; i < 3; i++) {
        *(result + i) = *(u + i) - *(v + i);
    }
}

// Compute vector c such that a × c = b and a · c = 3
// c is output array (pointer)
void compute_vector_c(double *c) {
    double a[3] = {1, 1, 1};
    double b[3] = {0, 1, -1};
    double a_cross_b[3];
    double three_a[3];
    double temp[3];

    cross(a, b, a_cross_b);
    scalar_mult(3.0, a, three_a);
    subtract(three_a, a_cross_b, temp);
    scalar_mult(1.0 / 3.0, temp, c);
}

