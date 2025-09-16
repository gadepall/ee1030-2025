#include <stdio.h>

// Function to compute dot product
double dot(double a[3], double b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// Function to compute cross product
void cross(double a[3], double b[3], double res[3]) {
    res[0] = a[1]*b[2] - a[2]*b[1];
    res[1] = a[2]*b[0] - a[0]*b[2];
    res[2] = a[0]*b[1] - a[1]*b[0];
}

// Function to compute u = a - (a·b)b
void compute_u(double a[3], double b[3], double u[3]) {
    double c = dot(a, b);
    for(int i=0;i<3;i++)
        u[i] = a[i] - c*b[i];
}

