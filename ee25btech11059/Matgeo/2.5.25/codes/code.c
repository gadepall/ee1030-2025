#include <stdio.h>

int dotProduct(int a[], int b[], int size) {
    int dot = 0;
    for (int i = 0; i < size; i++) {
        dot += a[i] * b[i];
    }
    return dot;
}

void scalarMultiply(int vector[], int scalar, int result[], int size) {
    for (int i = 0; i < size; i++) {
        result[i] = scalar * vector[i];
    }
}

void vectorSubtract(int a[], int b[], int result[], int size) {
    for (int i = 0; i < size; i++) {
        result[i] = a[i] - b[i];
    }
}

void solve_vectors() {
    int a[3] = {2, -1, -2};
    int b[3] = {7, 2, -3};

    int a_dot_b = dotProduct(a, b, 3);
    int a_dot_a = dotProduct(a, a, 3);

    int k = a_dot_b / a_dot_a;

    int b1[3];
    scalarMultiply(a, k, b1, 3);

    int b2[3];
    vectorSubtract(b, b1, b2, 3);

    printf("Vector a: [%d, %d, %d]\n", a[0], a[1], a[2]);
    printf("Vector b: [%d, %d, %d]\n", b[0], b[1], b[2]);
    printf("Scalar k: %d\n", k);
    printf("Vector b1 (parallel to a): [%d, %d, %d]\n", b1[0], b1[1], b1[2]);
    printf("Vector b2 (perpendicular to a): [%d, %d, %d]\n", b2[0], b2[1], b2[2]);
}
