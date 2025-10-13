// C code to calculate area of parallelogram
#include <stdio.h>
#include "libs/matfun.h"
#include <math.h>

double main(double *v1, double *v2) {
    // create a b vectros 
    double **a = createMat(3,1);
    a[0][0] = v1[0];
    a[1][0] = v1[1];
    a[2][0] = v1[2];

    double **b = createMat(3,1);
    b[0][0] = v2[0];
    b[1][0] = v2[1];
    b[2][0] = v2[2];


    double **a_cross_b = createMat(3,1);
    a_cross_b[0][0] = a[1][0] * b[2][0] - a[2][0] * b[1][0];
    a_cross_b[1][0] = a[2][0] * b[0][0] - a[0][0] * b[2][0];
    a_cross_b[2][0] = a[0][0] * b[1][0] - a[1][0] * b[0][0];

    double area = sqrt(Matdot(a_cross_b, a_cross_b, 3));

    printf("Area of the parallelogram (C): %lf\n", area);

    return area;

}