#include<stdio.h>

void check_ltm(int m, int n, double matrix[m][n]){
	if(m!=n)
	{
		printf("It is not a lower triangular matrix\n");
		return;
	}

	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++){
			if(j>i && matrix[i][j]!=0){
				printf("It is not a lower triangular matrix\n");
				return;
			}
		}
	}
	printf("It is a lower triangular matrix\n");
}



