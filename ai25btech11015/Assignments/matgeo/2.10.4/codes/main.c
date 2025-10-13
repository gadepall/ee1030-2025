
#include <stdio.h>
#include<math.h>
#include "libs/matfun.h"

void cross_product(double **a, double **b, double **result) {
    result[0][0] = a[1][0]*b[2][0] - a[2][0]*b[1][0];
    result[1][0] = a[2][0]*b[0][0] - a[0][0]*b[2][0];
    result[2][0] = a[0][0]*b[1][0] - a[1][0]*b[0][0];

}

double main(double *arr1 , double *arr2, double *arr3) {

	// printf("Vector A: [%f, %f, %f]\n", arr1[0], arr1[1], arr1[2]);
	double **A = createMat(3,1);
	double **B = createMat(3,1);	
	double **C = createMat(3,1);

	for(int i=0;i<3;i++){
		A[i][0] = arr1[i];
		B[i][0] = arr2[i];
		C[i][0] = arr3[i];
	}

	double **AB = createMat(3,1);
	double **AC = createMat(3,1);

	for(int i=0;i<3;i++){
		AB[i][0] = B[i][0] - A[i][0];
		AC[i][0] = C[i][0] - A[i][0];
	}

	// printf("Vector AB: [%f, %f, %f]\n", AB[0][0], AB[1][0], AB[2][0]);
	// printf("Vector AC: [%f, %f, %f]\n", AC[0][0], AC[1][0], AC[2][0]);

	double **cross = createMat(3,1);

	cross_product(AB,AC,cross);


	double area = 0.5 * Matnorm(cross,3);


	// printf("Cross Product: [%f, %f, %f]\n", cross[0], cross[1], cross[2]);
	// printf("Area of triangle ABC: %f\n", area);
	printf("Area of triangle ABC (C): %f\n", area);


	return area;
}
