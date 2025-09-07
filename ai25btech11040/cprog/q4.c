#include <stdio.h>

float avg (int numbers[]) {
	float sum = 0;
	for (int *i = &numbers[0]; i < &numbers[6]; i ++){
		sum += *i;
	}
	return sum/6;
}

int main(void){
	int scores[6] = {1555, 1670, 1750, 2013, 2540, 2820};
	printf("%f", avg(scores));
	return 0;
}
