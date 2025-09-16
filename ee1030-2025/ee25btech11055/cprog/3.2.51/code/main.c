// NCERT 3.2.51 - ee25btech11055

#include <stdio.h>

int main(void) {
	float a = 2.0/3.0, b = 5.0/2.0;

	if (a>b) {
		printf("%f > %f\n",a,b);
	} else if (a<b) {
		printf("%f < %f\n",a,b);
	} else {
		printf("%f = %f\n",a,b);
	}
	return 0;
}
