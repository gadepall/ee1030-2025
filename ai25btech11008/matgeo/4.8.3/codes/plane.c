#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    // Step 1: Define points A, B, C as 3x1 column vectors
    double **A = createMat(3,1);
    double **B = createMat(3,1);
    double **C = createMat(3,1);

    A[0][0] = 2;  A[1][0] = 5;  A[2][0] = -3;
    B[0][0] = -2; B[1][0] = -3; B[2][0] = 5;
    C[0][0] = 5;  C[1][0] = 3;  C[2][0] = -3;

    // Step 2: Compute AB = B - A, AC = C - A
    double **AB = Matsub(B, A, 3, 1);
    double **AC = Matsub(C, A, 3, 1);

    // Step 3: Form matrix [AB AC] (3x2)
    double **M = Mathstack(AB, AC, 3, 1, 1);

    // Step 4: Normal vector n = null space of Mᵀ
    // Compute n by solving (AB, AC) cross product equivalent
    double **n = createMat(3,1);
    n[0][0] = AB[1][0]*AC[2][0] - AB[2][0]*AC[1][0];
    n[1][0] = AB[2][0]*AC[0][0] - AB[0][0]*AC[2][0];
    n[2][0] = AB[0][0]*AC[1][0] - AB[1][0]*AC[0][0];

    // Step 5: Compute d = nᵀ * A
    double d = Matdot(n, A, 3);

    // Step 6: Save plane equation and points
    FILE *fp = fopen("plane_points.dat", "w");
    if (fp == NULL) {
        perror("Error opening file");
        return 1;
    }
    fprintf(fp, "# Plane equation: %lf*x + %lf*y + %lf*z = %lf\n",
            n[0][0], n[1][0], n[2][0], d);
    fprintf(fp, "%lf %lf %lf\n", A[0][0], A[1][0], A[2][0]);
    fprintf(fp, "%lf %lf %lf\n", B[0][0], B[1][0], B[2][0]);
    fprintf(fp, "%lf %lf %lf\n", C[0][0], C[1][0], C[2][0]);
    fclose(fp);

    // Step 7: Print only the 4 values for Python
    printf("%lf %lf %lf %lf\n", n[0][0], n[1][0], n[2][0], d);

    // Step 8: Free memory
    for(int i=0;i<3;i++){
        free(A[i]); free(B[i]); free(C[i]);
        free(AB[i]); free(AC[i]); free(M[i]); free(n[i]);
    }
    free(A); free(B); free(C);
    free(AB); free(AC); free(M); free(n);

    return 0;
}
