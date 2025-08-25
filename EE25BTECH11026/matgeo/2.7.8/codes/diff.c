#include<stdio.h>

double find_mag_diffvector(double a, double b ,double dot)
//Here dot is the dot product of a and b
{
	double val=a*a+b*b-2*dot;
	if(val<0) val=0;
	return sqrt(val);
}
