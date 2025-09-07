#include<stdio.h>
#include<math.h>

double norm(double *A, int m){
	double norm = 0;
	for(int i=0; i<m; i++){
		norm += A[i]*A[i];
	}
	norm = sqrt(norm);
	return norm;
}
