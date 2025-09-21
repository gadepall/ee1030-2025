#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif


#include "matfun.h"
#include "geofun.h"

int main(void) {
    // Allocate 2x1 matrices for points
    double **A = createMat(2,1);
    double **B = createMat(2,1);
    double **C = createMat(2,1);

   
    A[0][0] = -1; A[1][0] = 1;
    B[0][0] = 0; B[1][0] = 5;
    C[0][0] = 3; C[1][0] = 2;


    // Vectors B-A and C-A as 2x1 matrices
    double **BA = Matsub(B, A, 2, 1);
    double **CA = Matsub(C, A, 2, 1);

    // Extract components for clarity - correct matrix indexing
    double BAx = BA[0][0], BAy = BA[1][0];
    double CAx = CA[0][0], CAy = CA[1][0];


    // 2D cross product magnitude |(B-A) x (C-A)| = |BAx*CAy - BAy*CAx|
    double cp = fabs(BAx*CAy - BAy*CAx);
    double area = 0.5 * cp;

    // Save to points.dat
    FILE *fp = fopen("points.dat", "w");
    if (!fp) {
        perror("points.dat");
        // Clean up on error
        freeMat(BA, 2); freeMat(CA, 2);
        freeMat(A, 2); freeMat(B, 2); freeMat(C, 2);
        return 1;
    }
    
    fprintf(fp, "A %.1f %.1f\n", A[0][0], A[1][0]);
    fprintf(fp, "B %.1f %.1f\n", B[0][0], B[1][0]);
    fprintf(fp, "C %.1f %.1f\n", C[0][0], C[1][0]);
    fclose(fp);
    printf("Wrote points.dat\n");

    // Free memory
    freeMat(BA, 2); freeMat(CA, 2);
    freeMat(A, 2); freeMat(B, 2); freeMat(C, 2);
    
    return 0;
}
