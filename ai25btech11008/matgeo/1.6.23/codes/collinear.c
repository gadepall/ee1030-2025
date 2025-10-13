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

    // Set coordinates
    A[0][0] = 3.0;  A[1][0] = 1.0;
    B[0][0] = 6.0;  B[1][0] = 4.0;
    C[0][0] = 8.0;  C[1][0] = 6.0;

    // Calculate direction vectors B-A and C-A
    double **BA = Matsub(B, A, 2, 1);
    double **CA = Matsub(C, A, 2, 1);

    // Create matrix M = [BA | CA]
    double **M = createMat(2, 2);
    M[0][0] = BA[0][0];  M[0][1] = CA[0][0];
    M[1][0] = BA[1][0];  M[1][1] = CA[1][0];

    // Determinant
    double det = M[0][0]*M[1][1] - M[0][1]*M[1][0];
    if (fabs(det) < 1e-10) {
        printf("Points are collinear\n");
    } else {
        printf("Points are NOT collinear\n");
    }
    return 0;
}
