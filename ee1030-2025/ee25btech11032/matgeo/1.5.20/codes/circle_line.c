#include <math.h>

void circle_gen(double *X , double *Y , double *P, int n , double r)
{
// n is no. of points to generates. x stores x coor , y stores y coor 
    for (int i  = 0 ; i < n ; i++ )
    {
        double theta = 2.0 * M_PI * i / n ; 
        X[i] = P[0] + r * cos(theta);
        Y[i] = P[1] + r * sin (theta); 
    }   
}

void line_gen (double *X, double *Y , double *A , double *B , int n , int m )
{
    double temp[m] ; 
    for (int i = 0 ; i < m ; i++)
    {
        temp [ i ] = (B[i]- A[i]) /(double) n ; 
    }
    for (int i = 0 ; i <= n ; i++ )
    {
        X[i] = A[0] + temp[0] * i ; 
        Y[i] = A[1] + temp[1] * i ;
    }
}
