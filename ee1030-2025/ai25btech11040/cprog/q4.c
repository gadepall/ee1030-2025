#include <stdio.h>

int main(void){
	int scores[6] = {1555, 1670, 1750, 2013, 2540, 2820};
	float sum = 0;
	for (int i=0; i<6; i++) {
		sum += scores[i];
	}
	printf("%f", sum/6);
	return 0;
}
