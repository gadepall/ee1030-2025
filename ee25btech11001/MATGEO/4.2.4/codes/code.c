// code.c
#include <stdio.h>

// Generalized dot product of two n-dimensional vectors
int dot_product(const int* a, const int* b, int n) {
    int sum = 0;
    for(int i = 0; i < n; i++) {
        sum += a[i] * b[i];
    }
    return sum;
}

// Check if two n-dimensional vectors are orthogonal
int is_orthogonal(const int* a, const int* b, int n) {
    return dot_product(a, b, n) == 0;
}

// Compute normal vector of a 2D line Ax + By = C
// Returns result in nvec array (size 2)
void normal_vector(int A, int B, int* nvec) {
    nvec[0] = A;
    nvec[1] = B;
}

// Compute direction vector of a 2D line Ax + By = C
// Returns result in dvec array (size 2)
void direction_vector(int A, int B, int* dvec) {
    dvec[0] = B;
    dvec[1] = -A;
}
