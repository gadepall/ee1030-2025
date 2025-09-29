#include <stdio.h>

// Function to compute dot product of two 3D vectors
float dot_product(float v1[3], float v2[3]) {
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2];
}

// Function to check if A, B, C form a right-angled triangle
// Returns 1 if true, 0 otherwise
int is_right_triangle(float A[3], float B[3], float C[3]) {
    float AB[3], BC[3], AC[3];

    // Compute vectors
    AB[0] = B[0] - A[0];  AB[1] = B[1] - A[1];  AB[2] = B[2] - A[2];
    BC[0] = C[0] - B[0];  BC[1] = C[1] - B[1];  BC[2] = C[2] - B[2];
    AC[0] = C[0] - A[0];  AC[1] = C[1] - A[1];  AC[2] = C[2] - A[2];

    // Check dot products
    if (dot_product(AB, AC) == 0) {
        printf("∠A is 90 degrees.\n");
        return 1;
    }
    if (dot_product(AB, BC) == 0) {
        printf("∠B is 90 degrees.\n");
        return 1;
    }
    if (dot_product(AC, BC) == 0) {
        printf("∠C is 90 degrees.\n");
        return 1;
    }
    return 0;
}