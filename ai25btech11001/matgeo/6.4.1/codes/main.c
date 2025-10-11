
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
void matmul(int n, int k , int m, double a[n][k], double b[k][m], double c[n][m])
{
		for(int i = 0; i<n;i++)
				for(int j = 0; j<m;j++){c[i][j] = 0;
						for(int l = 0; l<k;l++)
								c[i][j]+=a[i][l]*b[l][j];
				}
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

void printMat(int n, int m , double x[n][m])
{
		printf("[\n");

		for(int i = 0; i<n;i++)
		{
				printf("[");
				for(int j = 0; j<m;j++)
						printf(" %lf ,",x[i][j]);
				printf("]\n");
		}
		printf("]\n");
}

void linearreg(int n, double x[1][n], double d[1][n],double r[2][1])
{
		double X[n][2];
		double D[n][1];
		double X_T[2][n];
		for(int i = 0; i<n;i++)
		{
				X[i][0] = 1;
				X[i][1] = x[0][i];
				D[i][0] = d[0][i];
				X_T[0][i] = 1;
				X_T[1][i] = x[0][i];
		}

		double X_TX [2][2];
		double X_TX_1 [2][2];
		matmul(2,n,2,X_T,X,X_TX);
		inv(2,X_TX,X_TX_1);
		double r_[2][1];
		matmul(2,n,1,X_T,D,r_);
		matmul(2,2,1,X_TX_1,r_,r);
}

double value(double n[2][1],double x)
{
		return n[0][0] + n[1][0]*x;
}

/*int main(){
		constexpr int n = 6;
		double X[1][n] = {{2001.0 ,2002.0 ,2003,2004,2005,2006}};
double D[1][n] = {{30,35,36,32,37,40}};
double N[2][1];
linearreg(n,X,D,N);
printf("%lf\n",X[0][3]);
printMat(2,1,N);
printf("%lf\n",value(N,2008));
return 0;
}*/
