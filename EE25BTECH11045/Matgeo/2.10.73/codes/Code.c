#include <stdio.h>
#include <math.h>

int main() {
    // Define B and C as given
    double B[3] = {0.5, sqrt(3)/2, 0};
    double C[3] = {0.5, -sqrt(3)/2, 0};
    double cross[3], A1[3], A2[3];

    // Cross product B x C
    cross[0] = B[1]*C[2] - B[2]*C[1];
    cross[1] = B[2]*C[0] - B[0]*C[2];
    cross[2] = B[0]*C[1] - B[1]*C[0];

    // A = ±2(B x C)
    for (int i=0; i<3; i++) {
        A1[i] = 2 * cross[i];
        A2[i] = -2 * cross[i];
    }

    // Print results
    printf("Vector B = (%.2f, %.2f, %.2f)\n", B[0], B[1], B[2]);
    printf("Vector C = (%.2f, %.2f, %.2f)\n", C[0], C[1], C[2]);
    printf("Cross Product (B x C) = (%.2f, %.2f, %.2f)\n", cross[0], cross[1], cross[2]);
    printf("A1 = +2(B x C) = (%.2f, %.2f, %.2f)\n", A1[0], A1[1], A1[2]);
    printf("A2 = -2(B x C) = (%.2f, %.2f, %.2f)\n", A2[0], A2[1], A2[2]);

    return 0;
}