#include<math.h>
#include<stdio.h>

double dot(double a[3],double b[3]){
	return a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
}

void plane(double arr[3]){
	double img[3];
	double n1[3]={1,-1,1};
	double norm_n_sq=3;
	
	for(int i=0;i<3;i++){
		img[i]=arr[i]-(2*(dot(arr,n1)-3)/norm_n_sq)*n1[i];
	}
	
	double b[2][3]={{img[0],img[1],img[2]},{1,2,1}};
	int k1;
	int k2;

	for(int i=0;i<3;i++){
		double p=b[0][0]+b[1][0];
		double q=b[0][1]+b[1][1];
		double r=b[0][2]+b[1][2];
		
		k2=(-1)/(b[1][2]-b[1][1]*(r/q));
		k1=(-1)*(r/q)*k2;
	}
	double n[3]={1,k1,k2};

	printf("(%.0lf)x+(%.0lf)y+(%.0lf)z=0",n[0],n[1],n[2]);
}
