
#include <math.h>
double solve(double a , double b, double c)
{
    double temp = sqrt(pow(b,2) - 4 * a  * c );
    if(temp == 0)
        return 1 ; 
    else
        return 0;
}
