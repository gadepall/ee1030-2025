#include <stdio.h>
#include <stdlib.h>
#include "geofun.h"
#include "matfun.h"

int main() {
    double k, det;
    double **A, **B, **C, **BA, **CA, **M;
    
    // Try for k=1 up to k=10 (just an example for solving; in practice, solve the equation)
    for (k = 1; k <= 10; k++) {
        // Allocate and fill points for this k
        A = createMat(2,1); B = createMat(2,1); C = createMat(2,1);
        A[0][0] = k+1;    A[1][0] = 2*k;
        B[0][0] = 3*k;    B[1][0] = 2*k+3;
        C[0][0] = 5*k-1;  C[1][0] = 5*k;
        // Compute BA and CA
        BA = Matsub(B, A, 2, 1);
        CA = Matsub(C, A, 2, 1);
        // Stack columns
        M = Mathstack(BA, CA, 2, 1, 1); // 2x2 matrix
        // Compute determinant
        det = Matdet(M);
        // If determinant is zero, we have rank 1 and thus collinear
        if (det == 0) {
            // Store to file as required
            FILE *fp = fopen("output.dat", "w");
            fprintf(fp, "%.0f %.0f\n", A[0][0], A[1][0]);
            fprintf(fp, "%.0f %.0f\n", B[0][0], B[1][0]);
            fprintf(fp, "%.0f %.0f\n", C[0][0], C[1][0]);
            fclose(fp);
        }
        // Free all allocated matrices
        freeMat(A,2); freeMat(B,2); freeMat(C,2);
        freeMat(BA,2); freeMat(CA,2); freeMat(M,2);
    }
    return 0;
}
