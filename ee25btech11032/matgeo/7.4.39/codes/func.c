#include <math.h>

double calc(double *X , double *Y , double c, double r)
{
    double temp1 , temp2 ,prod; 
    temp1 = (r*r + sqrt(pow(r,4) - 4 *  pow(c,4)))/2;
    temp2 = (r*r - sqrt(pow(r,4) - 4 *  pow(c,4)))/2; 

    X[0] = sqrt(temp1);
    X[1] = -sqrt(temp1);
    X[2] = sqrt(temp2);
    X[3] = -sqrt(temp2);
    prod = pow(sqrt(temp1),2) * pow(sqrt(temp2),2);
    for(int i = 0 ; i< 4 ; i++)
    {
        Y[i] = c*c/X[i] ;
    }
    return prod;

}
