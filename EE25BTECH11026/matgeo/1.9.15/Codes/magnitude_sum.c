#include<stdio.h>
#include<math.h>

double find_magnitude(int *result)
{
	double mag;
	mag=sqrt(pow(result[0],2)+pow(result[1],2)+pow(result[2],2));
	return mag;

}

void sum_of_vectors(int *a, int *b, int *c, int *result)
{
    for(int i = 0; i < 3; i++)
    {
        result[i] = a[i] + b[i] + c[i];
    }
}


