#include <stdio.h>
#include <math.h>
float formula(float *d,float *n)
{
    return asin((d[0]*n[0] + d[1]*n[1] + d[2]*n[2])/(sqrt(d[0]*d[0] + d[1]*d[1] + d[2]*d[2])*sqrt(n[0]*n[0] + n[1]*n[1] + n[2]*n[2])));
}