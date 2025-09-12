#include <math.h>
double norm_sq (double *P , double *Q , int m )
{
	double sum = 0 ; 
	for ( int i = 0 ; i  < m ; i++ )
		sum += pow(P[i] - Q[i] , 2);
	return sum ;
}

double ratio ( double *A , double *B , double *P , double norm  )
{
		double k = (A[0]-P[0]) * (P[0] - B[0]) + (A[1] - P[1]) * (P[1] - B[1]);
		k = k / norm;
		return k ; 
}
