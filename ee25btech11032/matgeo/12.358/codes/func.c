#include <stdio.h>
void row_mal(double A[2][4] , int n , int m, double k )
{
	for(int i = 0 ; i < 4 ;i++)
	{
		A[m][i] -= A[n][i]*k; 
	}
}
void row_div(double A[2][4] , int n , int m)
{
	double k = A[n][m]; 
	for(int i = 0 ; i  < 4 ; i++)
	{
		A[n][i] /= k ;
	}
}
void inv( double *A , double *B )
{
	double K[2][4]; 
	for(int i = 0 ; i < 2 ; i++)
	{
		K[i][0] = A[i]; 
		K[i][1] = B[i];
	}
	for(int i = 0 ; i < 2 ;  i++)
	{
	   K[i][i+2] = 1 ;
	}
	//print
		for(int i = 0 ; i  < 2 ; i++)
	{
	    
		for(int j = 0 ; j < 4; j++)
		{
		    if( j < 2){
			printf("%.1f ",K[i][j]);}
		}
		printf("\n");
	}	
	
	if(K[0][0] != 0  )
	{
		row_div(K , 0 , 0 );
		row_mal(K , 0 , 1 , K[1][0]);
			
	}
	else
	{
			if(K[1][0] != 0)
				row_mal(K,0,1,-1);
			row_div(K , 0 , 0 );
		  row_mal(K , 0 , 1 , K[1][0]);
		  		
	}
	if ( K[1][1] != 0  )
	{
		row_div(K , 1, 1);
		row_mal(K, 1, 0 , K[0][1]);
	}
	else
	{
		if(K[0][1] != 0 )
			row_mal(K, 1 , 0 , -1);
		
		row_div(K , 1, 1);
		row_mal(K, 1, 0 , K[0][1]);
	}
  printf("_____________________\n");
	for(int i = 0 ; i  < 2 ; i++)
	{   
	    
		for(int j = 0 ; j < 4; j++)
		{
		    if ( j >= 2){
			printf("%.3f ",K[i][j]);}
		}
		printf("\n");
	}	
}
