#include <stdio.h>

// Function to compute cross product of two vectors
void crossProduct(double u[], double v[], double result[]) {
    result[0] = u[1]*v[2] - u[2]*v[1];
    result[1] = u[2]*v[0] - u[0]*v[2];
    result[2] = u[0]*v[1] - u[1]*v[0];
}

// Function to compute dot product of two vectors
double dotProduct(double u[], double v[]) {
    return u[0]*v[0] + u[1]*v[1] + u[2]*v[2];
}

int main() {
    // Define vectors A = i, B = j, C = k
    double A[3] = {1, 0, 0};
    double B[3] = {0, 1, 0};
    double C[3] = {0, 0, 1};

    double BxC[3], CxA[3], AxC[3], AxB[3];
    double numerator1, denominator1, numerator2, denominator2, result;

    // Compute cross products
    crossProduct(B, C, BxC);
    crossProduct(C, A, CxA);
    crossProduct(A, C, AxC);
    crossProduct(A, B, AxB);

    // Compute terms
    numerator1 = dotProduct(A, BxC);
    denominator1 = dotProduct(CxA, B);
    numerator2 = dotProduct(B, AxC);
    denominator2 = dotProduct(C, AxB);

    // Final result
    result = (numerator1 / denominator1) + (numerator2 / denominator2);

    // Print results
    printf("Numerator1 = %.2f, Denominator1 = %.2f\n", numerator1, denominator1);
    printf("Numerator2 = %.2f, Denominator2 = %.2f\n", numerator2, denominator2);
    printf("Final Result = %.2f\n", result);

    return 0;
}
