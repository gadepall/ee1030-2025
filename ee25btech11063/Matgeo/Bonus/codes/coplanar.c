#include <stdio.h>

// Function to compute scalar triple product (box product)
float boxProduct(float A[3], float B[3], float C[3]) {
    return A[0] * (B[1]*C[2] - B[2]*C[1])
         - A[1] * (B[0]*C[2] - B[2]*C[0])
         + A[2] * (B[0]*C[1] - B[1]*C[0]);
}

int main() {
    FILE *fp;
    float A[3], B[3], C[3];
    float box;

    // Input 3 vectors
    printf("Enter vector A (x y z): ");
    scanf("%f %f %f", &A[0], &A[1], &A[2]);

    printf("Enter vector B (x y z): ");
    scanf("%f %f %f", &B[0], &B[1], &B[2]);

    printf("Enter vector C (x y z): ");
    scanf("%f %f %f", &C[0], &C[1], &C[2]);

    // Compute box product
    box = boxProduct(A, B, C);

    // Open file coplanar.dat for writing
    fp = fopen("coplanar.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(fp, "Scalar triple product (Box Product) = %.2f\n", box);

    if (box == 0)
        fprintf(fp, "Vectors are coplanar.\n");
    else
        fprintf(fp, "Vectors are NOT coplanar.\n");

    fclose(fp);

    printf("Result written to coplanar.dat\n");

    return 0;
}

