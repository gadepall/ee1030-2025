#include <stdio.h>
#include <math.h>

double Solve_for_y(double A[2], double B[2]){
	
	double y = ((pow(A[0],2) + pow(A[1],2)) - (pow(B[0],2) + pow(B[1],2)))/(2*(A[1] - B[1]));
	
	return y;
}
