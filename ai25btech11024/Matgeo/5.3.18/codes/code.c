#include<math.h>
#include<stdio.h>

void solve(double arr[3][3],double b[3]){
	double inv[3][3];

	inv[0][0]=(-1)*(arr[1][1]*arr[2][2]-arr[1][2]*arr[2][1]);
	inv[1][0]=arr[1][0]*arr[2][2]-arr[2][0]*arr[1][2];
	inv[2][0]=(-1)*(arr[1][0]*arr[2][1]-arr[2][0]*arr[1][1]);

	inv[0][1]=arr[0][1]*arr[2][2]-arr[2][1]*arr[0][2];
	inv[1][1]=(-1)*(arr[0][0]*arr[2][2]-arr[2][0]*arr[0][2]);
	inv[2][1]=arr[0][0]*arr[2][1]-arr[2][0]*arr[0][1];

	inv[0][2]=(-1)*(arr[0][1]*arr[1][2]-arr[1][1]*arr[0][2]);
	inv[1][2]=arr[0][0]*arr[1][2]-arr[1][0]*arr[0][2];
	inv[2][2]=(-1)*(arr[0][0]*arr[1][1]-arr[1][0]*arr[0][1]);

	double x,y,z;
	
	x=inv[0][0]*b[0]+inv[0][1]*b[1]+inv[0][2]*b[2];
	y=inv[1][0]*b[0]+inv[1][1]*b[1]+inv[1][2]*b[2];
	z=inv[2][0]*b[0]+inv[2][1]*b[1]+inv[2][2]*b[2];

	printf("x=%.1lf, y=%.1lf, z=%.1lf",x,y,z);
}
