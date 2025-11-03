#include <math.h>
void solve(double a , double b , double c , double *real , double *img)
{

	double temp = pow(b,2)- 4*a*c;
	if( temp >= 0 )
	{
		for(int i = 0 ; i < 2 ; i++)
		{
			real[i] = -b+pow((-1),i)*sqrt(temp);
			real[i] /=2 ;
		}
			
	}
	else
	{
		for(int i = 0 ; i< 2 ; i++)
		{
			real[i] = -b/2;
			img[i] = pow((-1),i)*sqrt(-temp)/2;
		}
	}
}
