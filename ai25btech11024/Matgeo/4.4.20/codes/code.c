#include<math.h>

double det(double a[2],double b[2]){
	return a[0]*b[1] - a[1]*b[0];
}

int line(double n[2],double a){
	double n1[2]={2,-5};
	double b=6;
	
	int flag=0;
	
	double c[2]={a,b};
	double x[2]={n[0],n1[0]};
	double y[2]={n[1],n1[1]};
	if(det(n,n1)==0){
		flag=1;
		if(det(x,c)==0 && det(y,c)==0){
			flag=2;
		}
	}

	return flag;
}
