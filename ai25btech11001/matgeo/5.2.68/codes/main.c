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

double* solve(int m, double v[m][m],double u[m])
{
		
	for(int i = 0; i<m; i++)
	{
			for(int j = 0; j<i;j++)
			{
				u[i]-=u[j]*v[i][j]/v[j][j];
				asub(v[i],v[j],m,v[i][j]/v[j][j]);
			}
	}
	for(int i = m-1; i>-1; i--)
	{
			for(int j = m-1; j>i;j--)
			{
				u[i]-=u[j]*v[i][j]/v[j][j];
				asub(v[i],v[j],m,v[i][j]/v[j][j]);
			}
	}
	for(int i = 0; i<m;i++)
		u[i]/=v[i][i];
		return u;
}

/*int main(){
		constexpr int n = 2;
	double vec[n][n] = {{ 2,3},
		{2,4}} ;
		double x[n] = {11,-24};
	solve(n,vec,x);
	for(int i = 0; i<n;i++)
	{
			//for(int j = 0; j<3;j++)
			printf("%lf ",x[i]);
	}
			printf("\n");

	return 0;
}*/
