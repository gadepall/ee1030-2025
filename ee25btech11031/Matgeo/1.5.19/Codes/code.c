#include <stdio.h>
#include <math.h>

float Solve_for_x(float x1, float y1, float x2, float y2){

//assuming that the point divides the line in ration k:1

	float k = -y1/y2;
	float x = (x1+k*x2)/(k+1);

	return x;
}
