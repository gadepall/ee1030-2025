#include<stdio.h>

void sub(int m, int n ,double a[m][n],int m0, int m1,double mul )
{
		for(int i = 0; i<n;i++)
				a[m0][i]-=a[m1][i]*mul;
				
}

double** rref(int m, int n ,double v[m][n])
{

	for(int i = 0; i<m; i++)
	{
			int a = -1;
			for(int j = 0; j<n;j++)
					if(v[i][j]!=0){a=j;break;}
			
		if(a==-1)continue;
			for(int j = 0; j<m;j++)
			{
					if(j==i)continue;
					sub(m,n,v,j,i,v[j][a]/v[i][a]);
			}
	}
	for(int i = 0; i<m; i++)
	{
			int a = -1;
			for(int j = 0; j<n;j++)
					if(v[i][j]!=0){a=j;break;}
		if(a==-1)continue;
			int k = v[i][a];
			for(int j = a; j<n;j++)
						v[i][j]/=k;
	}

	return (double**)v;
}

