#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif
#include "matfun.h"

int main(void) {
    // Allocate 2x1 matrices for points
    double **A = createMat(2,1);
    double **B = createMat(2,1);
    double **C = createMat(2,1);

    // Set points: A(-1,1), B(0,5), C(3,2)
    A[0][0] = -1.0; A[1][0] = 1.0;
    B[0][0] = 0.0; B[1][0] = 5.0;
    C[0][0] = 3.0; C[1][0] = 2.0;

    // Vectors B-A and C-A
    double **BA = Matsub(B, A, 2, 1);
    double **CA = Matsub(C, A, 2, 1);

    // Extract components
    double BAx = BA[0][0], BAy = BA[1][0];
    double CAx = CA[0][0], CAy = CA[1][0];

    // Cross product magnitude |(B-A) x (C-A)| = |BAx*CAy - BAy*CAx|
    double cp = fabs(BAx*CAy - BAy*CAx);
    double area = 0.5 * cp; // Triangle area

    // Save to points.dat
    FILE *fp = fopen("points.dat", "w");
    if (!fp) {
        perror("points.dat");
        freeMat(BA, 2); freeMat(CA, 2);
        freeMat(A, 2); freeMat(B, 2); freeMat(C, 2);
        return 1;
    }
    fprintf(fp, "# Point_Name X Y\n");
    fprintf(fp, "A %.1f %.1f\n", A[0][0], A[1][0]);
    fprintf(fp, "B %.1f %.1f\n", B[0][0], B[1][0]);
    fprintf(fp, "C %.1f %.1f\n", C[0][0], C[1][0]);
    fclose(fp);
    printf("Wrote points.dat\n");
    printf("Triangle area = %.2f\n", area);

    // Clean-up
    freeMat(BA, 2); freeMat(CA, 2);
    freeMat(A, 2); freeMat(B, 2); freeMat(C, 2);
    return 0;
}
