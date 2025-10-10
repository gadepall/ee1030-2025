#include<stdio.h>

void sub(int m, int n ,double a[m][n],int m0, int m1,double mul )
{
		for(int i = 0; i<n;i++)
				a[m0][i]-=a[m1][i]*mul;
				
}

int rank(int m, int n ,double v[m][n])
{
	int r=0;

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
	for(int i = 0; i<m;i++)
			for(int j = 0; j<n;j++)
					if(v[i][j] !=0){r+=1;break;}

	return r;
}

int main(){

	double vec[2][3] = 	{{-240,3,120},
		{-2,3./120.,1}} ;

	printf("%d\n",rank(2,3,vec));

	return 0;
}
