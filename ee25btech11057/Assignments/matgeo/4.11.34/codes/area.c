#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void solveIntersection(double a1,double b1,double c1,
                       double a2,double b2,double c2,
                       double *x,double *y) {
    double det = a1*b2 - a2*b1;
    *x = (b1*(-c2) - b2*(-c1)) / det;
    *y = (a2*(-c1) - a1*(-c2)) / det;
}

double triangleArea() {
    double x1,y1,x2,y2,x3,y3;

    // Line1 & Line2
    solveIntersection(3,-2,1, 2,3,-21,&x1,&y1);
    // Line2 & Line3
    solveIntersection(2,3,-21, 1,-5,9,&x2,&y2);
    // Line1 & Line3
    solveIntersection(3,-2,1, 1,-5,9,&x3,&y3);

    double area = 0.5 * fabs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2));
    return area;
}

