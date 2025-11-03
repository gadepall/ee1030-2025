#include<stdio.h>
#include<math.h>

void Calc_locus(double x1, double x2, double r1, double r2, double *a, double *b, double *c)
{
    *a=(r1+r2)/2.0;
    *c=fabs(x1 - x2)/2.0;
    *b = sqrt(pow(*a, 2) - pow(*c, 2));
}
