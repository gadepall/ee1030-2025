#include <stdio.h>
#include <math.h>

// Function to calculate determinant of 3x3 matrix
float determinant(float a[3][3]) {
    float det;
    det = a[0][0]*(a[1][1]*a[2][2] - a[1][2]*a[2][1])
        - a[0][1]*(a[1][0]*a[2][2] - a[1][2]*a[2][0])
        + a[0][2]*(a[1][0]*a[2][1] - a[1][1]*a[2][0]);
    return det;
}

// Function to compute dot product of two 3D vectors
float dot_product(float a[3], float b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

int main() {
    float v1[3] = {1, 1, 1};
    float v2[3] = {1, -1, 1};
    float v3[3] = {1, 1, -1};

    // Form matrix with vectors as columns
    float A[3][3] = {
        {v1[0], v2[0], v3[0]},
        {v1[1], v2[1], v3[1]},
        {v1[2], v2[2], v3[2]}
    };

    // 1. Check linear independence using determinant
    float det = determinant(A);
    printf("Determinant = %.2f\n", det);

    if (fabs(det) > 1e-6)
        printf("S is a linearly independent set.\n");
    else
        printf("S is NOT a linearly independent set.\n");

    // 2. Check if it is a basis for R^3
    if (fabs(det) > 1e-6)
        printf("S is a basis for R^3.\n");
    else
        printf("S is NOT a basis for R^3.\n");

    // 3. Check orthogonality
    float d12 = dot_product(v1, v2);
    float d13 = dot_product(v1, v3);
    float d23 = dot_product(v2, v3);

    printf("\nDot products:\n");
    printf("v1·v2 = %.2f\n", d12);
    printf("v1·v3 = %.2f\n", d13);
    printf("v2·v3 = %.2f\n", d23);

    if (fabs(d12) < 1e-6 && fabs(d13) < 1e-6 && fabs(d23) < 1e-6)
        printf("Vectors are orthogonal.\n");
    else
        printf("Vectors are NOT orthogonal.\n");

    // 4. Based on results, print the correct option
    printf("\nCorrect statement:\n");
    if (fabs(det) > 1e-6 && !(fabs(d12) < 1e-6 && fabs(d13) < 1e-6 && fabs(d23) < 1e-6))
        printf("Option (b): S is a basis for R^3.\n");
    else if (fabs(det) < 1e-6)
        printf("Option (a): S is not a linearly independent set.\n");
    else if (fabs(d12) < 1e-6 && fabs(d13) < 1e-6 && fabs(d23) < 1e-6)
        printf("Option (c): The vectors in S are orthogonal.\n");
    else
        printf("Option (d): An orthogonal set cannot be generated from S.\n");

    return 0;
}
