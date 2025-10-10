#include <stdio.h>
#include <math.h>
float formula(float *a,float *b)
{
    float c[3];
    c[0] = a[1]*b[2] - a[2]*b[1];
    c[1] = a[2]*b[0] - a[0]*b[2];
    c[2] = a[0]*b[1] - a[1]*b[0];
    
    return sqrt((c[0]*c[0] + c[1]*c[1] + c[2]*c[2]))/(sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])*sqrt(b[0]*b[0] + b[1]*b[1] + b[2]*b[2]));
}