#include<stdio.h>

void give_data(double *A, double *u, double *c, double *p, double *m, double *points){
    A[0] = 0; A[1] = 0; A[2] = 0; A[3] = 1;
    u[0] = -60; u[1] = 0;
    c[0] = -3600;
    p[0] = 0; p[1] = 30;
    m[0] = 1; m[1] = 1; 
    points[0] = 1; points[1] = -120; points[2] = -3600; points[3] = 1; points[4] = 30;
}