#include<stdio.h>
#include<math.h>

void find_pts(int r) //Enter the square of radius
{
	int x= (int)(sqrt(r-2));
	printf("The points are (%d,0) and (%d, 0)\n",x, -x);
	return;
}
