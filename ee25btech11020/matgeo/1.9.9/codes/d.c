#include<stdio.h>
#include <math.h>
double distance(double *a,double *b, int n)
{
	double d=0;
	for(int i=0;i<n;i++)
	{
		d=d+pow(a[i]-b[i],2);
	}
	d=sqrt(d);
	return d;
}
