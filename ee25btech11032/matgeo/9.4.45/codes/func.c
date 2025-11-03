
#include <math.h>
double solve(double a , double b, double c)
{
    double temp = sqrt(pow(b,2) - 4 * a  * c );
    double res = (-1 * b + temp )/2 ; 
    if ( res >= 0 )
        return res;
    res = (-1*b - temp)/2;
    return res;
}
