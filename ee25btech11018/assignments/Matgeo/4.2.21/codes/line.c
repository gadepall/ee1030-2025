#include <stdio.h>

// Calculate dot product of two 2D vectors
int dot_product(int a[2], int b[2]) {
    return a[0]*b[0] + a[1]*b[1];
}

// Check if vectors are orthogonal (dot product = 0)
int is_orthogonal(int a[2], int b[2]) {
    return dot_product(a, b) == 0;
}

// Given the x-coordinate, calculate the corresponding y on the line
double line_equation(double x) {
    return (9.0*x)/5.0 + 32.0;
}


