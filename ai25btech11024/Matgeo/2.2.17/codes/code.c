#include<stdio.h>
#include <math.h>

double angle(double *a,double *b) {

    double PI=acos(-1);

    double dot = a[0]*b[0] + a[1]*b[1];
    double norm_a = sqrt(a[0]*a[0] + a[1]*a[1]);
    double norm_b = sqrt(b[0]*b[0] + b[1]*b[1]);

    double theta = acos(dot / (norm_a * norm_b));  // radians
    return theta * 180.0 / PI;  // convert to degree
}
