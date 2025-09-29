void section_formula ( double *X , double *Y , double *A , double ratio , int m  )
{
	for(int i = 0;  i < m ; i++)	
			A[i] = (1/(1+ratio))*(X[i] + ratio * Y[i] );
}
