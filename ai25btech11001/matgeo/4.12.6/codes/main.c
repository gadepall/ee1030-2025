#include<stdio.h>

int rank(int m, int n ,double v[m][n])
{
	int r=m;

	for(int i = m-1; i>-1; i--)
	{
		for(int j = 0 ; j<i;j++){
		double d = v[i][0]/v[j][0];
		int b = 1;
		for(int k = 1; k<n;k++)
		{
			if(d*v[j][k] != v[i][k]){b=0; break;}
		}
		if(b){r-=1;
		break;}
		}
	}

	return r;
}
/*
int main(){

	double vec[2][3] = 	{{-240,3,120},
		{-2,3./120.,1}} ;

	printf("%d\n",rank(2,3,vec));

	return 0;
}*/
