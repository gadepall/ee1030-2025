//Code by Darsh Gajare
//August 19, 2025
//Listing prime factors of a number
#include <stdio.h>
#include <math.h>
int main(void)
{
	int a=540;
	int count;
	for(int i=2; i<=a;i++)
	{
		count=0;
		while(a%i==0)
		{
			count++;
			a/=i;
		}
		if(count!=0)
		printf("%d^%d  ",i,count);
	}
	printf("\n");
	return 0;
}
