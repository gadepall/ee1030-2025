#include <stdio.h>
#include <math.h>
void mag(int n,double M,double *a,double *b){
	double sum=0.0;
	for(int i=0;i<n;i++)
		sum=sqrt(pow(a[i],2)+pow(sum,2));
	for(int i=0;i<n;i++)
		b[i]=a[i]*(M/sum);
}
