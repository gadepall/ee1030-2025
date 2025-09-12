#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

int main(void) {
    // Points as 2x1 column vectors
    double **A = createMat(2,1);
    double **B = createMat(2,1);
    double **C = createMat(2,1);

    // Set coordinates correctly
    A[0][0] = 2.0;  A[1][0] = 1.0;
    B[0][0] = 0.0;  B[1][0] = 5.0;
    C[0][0] = -1.0; C[1][0] = 2.0;

    // Calculate direction vectors B-A and C-A
    double **BA = Matsub(B, A, 2, 1);
    double **CA = Matsub(C, A, 2, 1);

    // Create matrix M manually as a 2x2 matrix [BA | CA]
    double **M = createMat(2, 2);
    
    // Fill M with BA and CA as columns
    M[0][0] = BA[0][0];  M[0][1] = CA[0][0];
    M[1][0] = BA[1][0];  M[1][1] = CA[1][0];

    // Calculate determinant to find rank
    double det = M[0][0] * M[1][1] - M[0][1] * M[1][0];
    
    int rank;
    if (fabs(det) > 1e-10) {  // Use fabs for absolute value
        rank = 2;
    } else {
        // Check if at least one row is non-zero
        if ((fabs(M[0][0]) > 1e-10 || fabs(M[0][1]) > 1e-10) || 
            (fabs(M[1][0]) > 1e-10 || fabs(M[1][1]) > 1e-10)) {
            rank = 1;
        } else {
            rank = 0;
        }
    }

    // Output result
    if (rank == 2) {
        printf("The points A, B, and C are NOT collinear (Rank = 2)\n");
    } else if (rank == 1) {
        printf("The points A, B, and C are collinear (Rank = 1)\n");
    } else {
        printf("All points coincide (Rank = 0)\n");
    }

    // Write points to .dat file
    FILE *f = fopen("points.dat", "w");
    if (f == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    fprintf(f, "%.6f\t%.6f\n", A[0][0], A[1][0]);
    fprintf(f, "%.6f\t%.6f\n", B[0][0], B[1][0]);
    fprintf(f, "%.6f\t%.6f\n", C[0][0], C[1][0]);
    fclose(f);

    printf("Points written to points.dat\n");

    // Free memory
    freeMat(A, 2);
    freeMat(B, 2);
    freeMat(C, 2);
    freeMat(BA, 2);
    freeMat(CA, 2);
    freeMat(M, 2);

    return 0;
}

