#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

int main(){
	int n=2;
	double **A, **b, **A_inv, **x;

	A=createMat(n,n);
	b=createMat(n,1);
	x=createMat(n,1);


	A[0][0]=1; A[0][1]=1;
	A[1][0]=3; A[1][1]=0;

	b[0][0]= -13;
	b[1][0]= 0;

	A_inv = Matinv(A,n);

	x=Matmul(A_inv,b,n,n,1);

	printf("Solution of Ax=b:\n");
	for(int i=0;i<n;i++){
		printf("x[%d]=%.2f\n", i+1, x[i][0]);
	}

	FILE *file=fopen("values.dat", "w");
	if(file==NULL){
		printf("Error opening file!\n");
		return 1;
	}

	fprintf(file, "The point of intersection of the line segment and the Y-axis is:\n");
		fprintf(file, "x-coordinate    y-coordinate\n");
		fprintf(file, "   %.2f              %.2f",x[0][0], x[1][0]);


	fclose(file);
	printf("Results have been written to values.dat\n");

	freeMat(A,n);
	freeMat(b,n);
	freeMat(A_inv,n);
	freeMat(x,n);

	return 0;

}
