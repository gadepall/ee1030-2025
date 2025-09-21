#include <stdio.h>
#include <math.h>

void dot_product(double vector1[], double vector2[], int size, double* result) {
    *result = 0.0;
    for (int i = 0; i < size; i++) {
        *result += vector1[i] * vector2[i];
    }
}


