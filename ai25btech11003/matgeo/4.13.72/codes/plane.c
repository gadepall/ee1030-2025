
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Function to compute cross product of two 3D vectors
void cross_product(double a[3], double b[3], double result[3]) {
    result[0] = a[1] * b[2] - a[2] * b[1];
    result[1] = a[2] * b[0] - a[0] * b[2];
    result[2] = a[0] * b[1] - a[1] * b[0];
}

// Function to compute dot product of two 3D vectors
double dot_product(double a[3], double b[3]) {
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
}

// Function to compute vector magnitude
double vector_magnitude(double v[3]) {
    return sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2]);
}
