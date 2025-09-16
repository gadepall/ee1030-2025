#include <stdio.h>
#include <math.h>

// Function to compute dot product
void dot_product(double v1[], double v2[], int size, double* result) {
    *result = 0.0;
    for (int i = 0; i < size; i++) {
        *result += v1[i] * v2[i];
    }
    return result;
}
