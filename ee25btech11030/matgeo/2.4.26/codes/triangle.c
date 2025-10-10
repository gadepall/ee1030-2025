#include <stdio.h>

void isosceles_triangle(double *points,double *M) {
    double coords[8] = {5,-2,  6,4,  7,-2, 6,-2};

    for (int i = 0; i < 6; i++) {
        points[i] = coords[i];
    }
    M[0]=coords[6];
    M[1]=coords[7];
}
