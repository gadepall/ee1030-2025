#include<stdio.h>


void inv(float matrix[2][2] , float inverse[2][2]){

	float det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];

	float invDet = 1.0 / det;

    inverse[0][0] =  matrix[1][1] * invDet;
    inverse[0][1] = -matrix[0][1] * invDet;
    inverse[1][0] = -matrix[1][0] * invDet;
    inverse[1][1] =  matrix[0][0] * invDet;
}



int main(){
	float A[2][2] = {{1,1},{-1,1}};
	float B[2]={180,44};
	float invA[2][2];
	float X[2];

	inv(A,invA);

	X[0]=invA[0][0]*B[0] + invA[0][1]*B[1];
	X[1]=invA[1][0]*B[0] + invA[1][1]*B[1];

	printf("Smaller angle = %.2f degrees\n",X[0]);
	printf("Larger angle = %.2f degrees\n",X[1]);

	return 0;
	}

