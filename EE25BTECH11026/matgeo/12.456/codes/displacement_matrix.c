#include<stdio.h>

void displacement_matrix(double *matrix, double gamma){
	matrix[0]=1;
	matrix[1]=gamma;
	matrix[2]=0;
	matrix[3]=1;
}
