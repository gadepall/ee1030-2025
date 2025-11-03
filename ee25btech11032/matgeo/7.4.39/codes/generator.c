#include <math.h>

void circle_gen(double *X , double *Y , double *P, int n , double r)
{
 
    for (int i  = 0 ; i < n ; i++ )
    {
        double theta = 2.0 * M_PI * i / n ; 
        X[i] = P[0] + r * cos(theta);
        Y[i] = P[1] + r * sin (theta); 
    }   
}

void points_gen (double *X , double a , double b , int n )
{
    double temp = (b - a )/(double)n ; 
    for (int i = 0 ; i <= n ; i++ )
    {
        X[i] = a + temp * i ; 
    }
}
void hyper_gen (double *X , double *Y , double c , int n )
{
    for(int i = 0; i < n ;i++)
    {
        Y[i] = c*c/X[i];
    }
}

