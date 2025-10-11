#include <stdio.h>
void row_mal(double A[3][6] , int n , int m, double k )
{
	for(int i = 0 ; i < 6 ;i++)
	{
		A[m][i] -= A[n][i]*k; 
	}
}
void row_div(double A[3][6] , int n , int m)
{
	double k = A[n][m]; 
	for(int i = 0 ; i  <6 ; i++)
	{
		A[n][i] /= k ;
	}
}
void inv( double *A , double *B , double *C  )
{
	double K[3][6]; 
	for(int i = 0 ; i < 3 ; i++)
	{
		K[i][0] = A[i]; 
		K[i][1] = B[i];
		K[i][2] = C[i];
	}
	for(int i = 0 ; i < 3 ;  i++)
	{
	   // K[i][i] = 1 ;
		for(int j = 3 ; j < 6 ; j++){
			if( j-3  == i )
				K[i][j] = 1 ;
			else
				K[i][j] = 0 ; 
		}
	}
	//print
		for(int i = 0 ; i  < 3 ; i++)
	{
	    
		for(int j = 0 ; j < 6; j++)
		{
		    if( j < 3){
			printf("%.1f ",K[i][j]);}
		}
		printf("\n");
	}	
	
	if(K[0][0] != 0  )
	{
		row_div(K , 0 , 0 );
		row_mal(K , 0 , 1 , K[1][0]);
		row_mal(K , 0 , 2 , K[2][0]);		
	}
	else
	{
			if(K[1][0] != 0)
				row_mal(K,0,1,-1);
			else if(K[2][0] != 0)
				row_mal(K,0,2,-1);
		  row_div(K , 0 , 0 );
		  row_mal(K , 0 , 1 , K[1][0]);
		  row_mal(K , 0 , 2 , K[2][0]);		
	}
	if ( K[1][1] != 0  )
	{
		row_div(K , 1, 1);
		row_mal(K, 1, 0 , K[0][1]);
		row_mal(K , 1, 2 , K[2][1]);
	}
	else
	{
		if(K[0][1] != 0 )
			row_mal(K, 1 , 0 , -1);
		else if(K[2][1] != 0 )
			row_mal(K, 1 , 2 ,-1);
		row_div(K , 1, 1);
		row_mal(K, 1, 0 , K[0][1]);
		row_mal(K , 1, 2 , K[2][1]);

	}
	if (K[2][2] != 0  )
	{
		row_div(K , 2, 2);
		row_mal(K, 2, 0 , K[0][2]);
		row_mal(K , 2, 1 , K[1][2]);
	}
	else
	{
		if(K[0][2] != 0 )
			row_mal(K,2 , 0 , -1);
		else if(K[1][2] != 0 )
			row_mal(K,2,1,-1);
		row_div(K , 2, 2);
		row_mal(K, 2, 0 , K[0][2]);
		row_mal(K , 2, 1 , K[1][2]);
	}
  printf("_____________________\n");
	for(int i = 0 ; i  < 3 ; i++)
	{   
	    
		for(int j = 0 ; j < 6; j++)
		{
		    if ( j >= 3){
			printf("%.3f ",K[i][j]);}
		}
		printf("\n");
	}	
}
