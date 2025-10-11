#include<stdio.h>
#include<math.h>
double dot(double *a, double *b) {
    double r=0;
    for(int i=0;i<3;i++)
        r += a[i]*b[i];
    return r;
}
double norm(double *a) {
    return sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2]);
}
double angle_deg(double *a, double *b) {
    double d = dot(a, b);
    double n1 = norm(a);
    double n2 = norm(b);
    double ratio = d/(n1*n2);
    if (ratio > 1) ratio=1;
    if (ratio < -1) ratio=-1;
    return acos(ratio)*180.0/M_PI;
}
int collinear(double *a, double *b) {
    double ang = angle_deg(a, b);
    return (ang < 1e-8 || fabs(ang - 180) < 1e-8);
}
