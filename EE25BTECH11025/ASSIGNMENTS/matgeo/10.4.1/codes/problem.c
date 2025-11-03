#include <stdio.h>

void give_data(double *A, double *u, double *c, double *p, double *m, double *points){

    A[0] = 16.0/145.0; 
    A[1] = 0; 
    A[2] = 0; 
    A[3] = 9.0/145.0;  

    u[0] = 0; 
    u[1] = 0;

    c[0] = -1;   
    p[0] = 2; 
    p[1] = 3;


    m[0] = 32 * 2;
    m[1] = 18 * 3; 
    points[0] = A[0];
    points[1] = A[3];
    points[2] = c[0];
    points[3] = p[0];
    points[4] = p[1];
}
