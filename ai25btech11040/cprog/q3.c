#include <stdio.h>
#include <math.h>

float amt(float ppl, float interest) {
	return ppl*pow(1+interest/100,3);
}

int main(void) {
	printf("a) %f\nb) %f\n", amt(1200,12),amt(7500,5));
}
