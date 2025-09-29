// C code to calculate area of parallelogram
#include <stdio.h>
#include "libs/matfun.h"
#include <math.h>

double main() {
    // create a b vectros 
    double **a = createMat(3,1);
    a[0][0] = 3;
    a[1][0] = 1;
    a[2][0] = 4;

    double **b = createMat(3,1);
    b[0][0] = 1;
    b[1][0] = -1;
    b[2][0] = 1;


    double **a_cross_b = createMat(3,1);
    a_cross_b[0][0] = a[1][0] * b[2][0] - a[2][0] * b[1][0];
    a_cross_b[1][0] = a[2][0] * b[0][0] - a[0][0] * b[2][0];
    a_cross_b[2][0] = a[0][0] * b[1][0] - a[1][0] * b[0][0];

    double area = sqrt(Matdot(a_cross_b, a_cross_b, 3));

    printf("Area of the parallelogram: %lf\n", area);

    FILE *fp = fopen("var.dat", "w");
    if (fp != NULL) {
        fprintf(fp, "%lf\n", area);
        fclose(fp);
    } else {
        printf("Error opening file for writing.\n");
    }
    


    return area;

}