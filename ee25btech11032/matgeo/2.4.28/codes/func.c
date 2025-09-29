
#include <math.h>
double norm_vec_sq(double *A , int m )
{
    double sum = 0.0; 
    for ( int i = 0 ; i < m ; i++ )
    {
        sum += pow(A[i] , 2 );
    }
    return sum; 
}

double x_cal(double *A , double *B , double *E , double na , double nb  )
{
    double x , k ; 
    k = (A[0]-B[0])*E[0] + (A[1]-B[1])*E[1];  
    x = (na - nb) / (2*k);
    return x; 
}
