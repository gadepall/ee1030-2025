#include <math.h>
double length(double *A , double *B , int m )
{
    double sum = 0.0; 
    for ( int i = 0 ; i < m ; i++ )
    {
        sum += pow(A[i]-B[i] , 2 );
    }
    return sqrt(sum) ; 
}
