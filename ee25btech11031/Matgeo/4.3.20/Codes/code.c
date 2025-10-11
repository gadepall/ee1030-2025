#include <stdio.h>
#include <math.h>

double Solve_for_y(double A[2], double B[2]){
	
	double k = -A[0]/B[0];
	double y = (A[1]+(k*B[1]))/(k+1);

	return y;
}
