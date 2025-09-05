#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include"libs/matfun.h"
#include"libs/geofun.h"
int main()
{
	double **A, **B, **P, **D1,**D2,**t;
	double xa=2.0,ya=3.0,xb=7.0,yb=8.0,xp=4.0,yp=5.0,k;
	A=createMat(2,1);
	B=createMat(2,1);
	P=createMat(2,1);
	D1=createMat(2,1);
	D2=createMat(2,1);
	A[0][0]=xa;
	A[1][0]=ya;
	B[0][0]=xb;
	B[1][0]=yb;
	P[0][0]=xp;
	P[1][0]=yp;
	D1=Matsub(A,P,2,1);
	D2=Matsub(P,B,2,1);
	t=transposeMat(D1,2,1);
	k=Matmul(t,D2,1,2,2)[0][0]/pow(Matnorm(D2,2),2);
	FILE *fptr;
		fptr=fopen("data.dat","w");
	if(fptr==NULL){
		printf("Error opening file");
		return 1;
	}
	
		fprintf(fptr,"k=%.02f",k);
		fclose(fptr);
	return 0;
}
