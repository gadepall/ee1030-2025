#include<stdio.h>
#include<math.h>

void roots(double a, double b, double c, double* x, double* y)
{
	double det= sqrt(b*b - 4*a*c);
	*x= (-b + det)/(2*a);
	*y=(-b -det)/(2*a);
}
