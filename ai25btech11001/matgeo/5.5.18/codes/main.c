#include<stdio.h>
#include<stdlib.h>

void asub(double* a,const double* b, int s, double mul)
{
		for(int i = 0; i<s;i++)
				a[i]-=mul*b[i];
}
void adiv(double* a, int s,double div)
{
		for(int i = 0; i<s;i++)
				a[i]/=div;
}

void inv(int m, double v[m][m],double a[m][m])
{
		for(int i = 0;i<m;i++)
				for(int j = 0; j<m;j++)
						a[i][j]=(i==j?1:0);
		

	for(int i = 0; i<m; i++)
	{
			for(int j = 0; j<i;j++)
			{
				asub(a[i],a[j],m,v[i][j]/v[j][j]);
				asub(v[i],v[j],m,v[i][j]/v[j][j]);
			}
	}
	for(int i = m-1; i>-1; i--)
	{
			for(int j = m-1; j>i;j--)
			{
				asub(a[i],a[j],m,v[i][j]/v[j][j]);
				asub(v[i],v[j],m,v[i][j]/v[j][j]);
			}
	}
	for(int i = 0; i<m;i++)
		adiv(a[i],m,v[i][i]);

}

/*int main(){

	double vec[3][3] = 	{{ 2,3,1},
		{2,4,1},{3,7,2}} ;
	double** a = inv(3,vec);
	for(int i = 0; i<3;i++)
	{
			for(int j = 0; j<3;j++)
			printf("%lf ",a[i][j]);
			printf("\n");
	}
	freeMat(3,a);

	return 0;
}*/
