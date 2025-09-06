#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include"libs/matfun.h"
#include"libs/geofun.h"
int main()
{
	double **A, **B, **C, **R,**t;
	double xa=1.0,ya=-2.0,za=1.0,xb=-2.0,yb=4.0,zb=5.0,xc=1.0,yc=-6.0,zc=-7.0;
	A=createMat(3,1);
	B=createMat(3,1);
	C=createMat(3,1);
	R=createMat(3,1);
	A[0][0]=xa;
	A[1][0]=ya;
	A[2][0]=za;
	B[0][0]=xb;
	B[1][0]=yb;
	B[2][0]=zb;
	C[0][0]=xc;
	C[1][0]=yc;
	C[2][0]=zc;
	R=Matadd(A,B,3,1);
	R=Matadd(R,C,3,1);
	FILE *fptr;
		fptr=fopen("data.dat","w");
	if(fptr==NULL){
		printf("Error opening file");
		return 1;
	}
	for (int i = 0; i < 3; i++) {
        fprintf(fptr, "%.2f ", R[i][0]);
    }
		fclose(fptr);
	return 0;
}
