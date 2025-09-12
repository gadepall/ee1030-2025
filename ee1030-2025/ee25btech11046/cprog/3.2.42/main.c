#include <stdio.h>
int main(){
	float a=-4.0/3.0, b=-3.0/2.0, c;
	int n1=-4, n2=3, d1=3, d2=2;
	if (a<b){
		printf("-%d/%d < -%d/%d", n1, d1, n2, d2);
	}
	else if (a>b){
		printf("-%d/%d > -%d/%d", n1, d1, n2, d2);
	}
	else if (a==b){
		printf("-%d/%d = -%d/%d", n1, d1, n2, d2);
	}
}
