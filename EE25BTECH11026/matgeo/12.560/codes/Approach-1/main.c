#include<stdio.h>

void dir_vec(double x, double y, double *grad){
	grad[0]=2*x;
	grad[1]=2*y;
}
