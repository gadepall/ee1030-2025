#include <stdio.h>

int main(void) {
	float a = 2.0/3.0;
	float b = 5.0/2.0;

	(a>b) ? printf("%f > %f\n",a,b) :
		(a<b) ? 
		printf("%f < %f\n",a,b) : 
		printf("%f = %f", a, b);
	return 0;
}
