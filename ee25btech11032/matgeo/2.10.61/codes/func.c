
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



