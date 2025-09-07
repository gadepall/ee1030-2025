#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "matfun.h"   // For createMat, freeMat
#include "geofun.h"
int main() {
    // Define points as column vectors
    double **A, **B;
    double dx, dy, diagonal;

    // Allocate 2x1 matrices for A and B
    A = createMat(2, 1);
    B = createMat(2, 1);

    // A = (0,3), B = (5,0)
    A[0][0] = 0;   A[1][0] = 3;
    B[0][0] = 5;   B[1][0] = 0;

    



    // Calculate diagonal length = ||A - B||
    dx = A[0][0] - B[0][0];
    dy = A[1][0] - B[1][0];
    diagonal = sqrt(dx*dx + dy*dy);

    printf("Length of diagonal AB = %.2lf\n", diagonal);

    // Free matrices
    freeMat(A, 2);
    freeMat(B, 2);

    return 0;
}
