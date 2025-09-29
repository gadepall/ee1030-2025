#include <stdio.h>
#include <stdlib.h>
#include "matfun.h"

int main() {
    double **M, **k, **C;
    int cx = 2, cy = 0;  // Center of circle
    int ax = 6, ay = 0;  // One endpoint of diameter

    // Create matrices: M (2x2), k (2x1), C (2x1)
    M = createMat(2, 2);
    k = createMat(2, 1);

    // Arrange matrix M: columns are points C and A
    M[0][0] = (double)cx; M[1][0] = (double)cy;
    M[0][1] = (double)ax; M[1][1] = (double)ay;

    // Weights vector for B = 2*C - A
    k[0][0] = 2.0;
    k[1][0] = -1.0;

    // Calculate B = M * k
    C = Matmul(M, k, 2, 2, 1);

    // Print result B
    printf("Coordinates of other end B = (%.2lf, %.2lf)\n", C[0][0], C[1][0]);

    // Free allocated matrices
    freeMat(M, 2);
    freeMat(k, 2);
    freeMat(C, 2);

    return 0;
}
