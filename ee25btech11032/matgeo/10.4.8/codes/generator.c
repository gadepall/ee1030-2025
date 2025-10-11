#include <math.h>
void linegen(double *XY, double *A , double *B , int n , int m )
{
    double temp[m] ; 
    for (int i = 0 ; i < m ; i++)
    {
        temp [ i ] = (B[i]- A[i]) /(double) n ; 
    }
    for (int i = 0 ; i < n ; i++ )
        for (int j = 0 ; j < m ; j++)
            XY[j*n + i ] = A[j] + temp[j] * i ; 
}          
void points_gen (double *X , double a , double b , int n )
{
    double temp = (b - a )/(double)n ; 
    for (int i = 0 ; i <= n ; i++ )
    {
        X[i] = a + temp * i ; 
    }
}
void parabola(double *X , double *Y , double a , int n)
{
    for(int i = 0 ; i < n ; i++)
    {
        Y[i] = sqrt(4*a*X[i]); 
        
    }
}
