#include <stdio.h>
#include <math.h>

// Function to compute dot product
void dot_product(double vector1[], double vector2[], int size, double* result) {
    *result = 0.0;
    for (int i = 0; i < size; i++) {
        *result += vector1[i] * vector2[i];
    }
}

// Function to compute squared distance between two 2D points using dot product
void distance_squared(double A[2], double B[2], double* result) {
    double AB[2];
    AB[0] = B[0] - A[0];   // x2 - x1
    AB[1] = B[1] - A[1];   // y2 - y1
    dot_product(AB, AB, 2, result); // AB · AB
}
