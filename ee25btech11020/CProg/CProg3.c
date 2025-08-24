//Code by Darsh Gajare
//August 18, 2025
//Range of Third side of triangle
#include <stdio.h>
//begin main function
int main(void)
{
	//declaring variables
	int a=6, b=8;
	if(b>a)
		printf("Range of third side is %d to %d\n",b-a,a+b);
	else
		printf("Range of third side is %d to %d\n", a-b,a+b);
}
