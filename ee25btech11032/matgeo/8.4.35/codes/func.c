
#include <math.h>
double e_val(double a , double b)
{
    if(a<b)
        return sqrt(1-pow(a,2)/pow(b,2));
    else
        return sqrt(1-pow(b,2)/pow(a,2));

}
