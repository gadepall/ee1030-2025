#include <stdio.h>
void formula(double *a,double *b)
{
   double x, y;
   a[0] = a[0]/a[1];
   a[1] = 1;
   b[0] = 1;
   b[1] = -a[0]; 
}