#include <math.h>
void solve(double a , double b , double c , double *X)
{
	double temp = sqrt(pow(b,2)- 4*a*c);
	for(int i = 0 ; i< 2 ; i++)
	{
		X[i] = -b+pow((-1),i)*temp;
		X[i] /=2 ;
	}
}
