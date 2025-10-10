#include <stdio.h>
#include "matfun.h"
#include "geofun.h"

int main() {
    double **A = createMat(2,1);
    double **B = createMat(2,1);
    double **C = createMat(2,1);

    A[0][0] = 1;   A[1][0] = 3;
    B[0][0] = -1;  B[1][0] = 2;
    C[0][0] = 2;   C[1][0] = 5;

    double **AplusC = Matadd(A, C, 2, 1);
    double **D = Matsub(AplusC, B, 2, 1);

    // Write all vertices to output.dat for plotting
    FILE *f = fopen("output.dat", "w");
    if (f != NULL) {
        fprintf(f, "%lf %lf\n", A[0][0], A[1][0]);
        fprintf(f, "%lf %lf\n", B[0][0], B[1][0]);
        fprintf(f, "%lf %lf\n", C[0][0], C[1][0]);
        fprintf(f, "%lf %lf\n", D[0][0], D[1][0]);
        fclose(f);
    } else {
        printf("Error opening output.dat for writing.\n");
    }

    // Free memory
    freeMat(A, 2);
    freeMat(B, 2);
    freeMat(C, 2);
    freeMat(AplusC, 2);
    freeMat(D, 2);

    return 0;
}
