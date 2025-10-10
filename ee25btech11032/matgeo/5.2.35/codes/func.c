void gaussian(double *A , double *B , double *C , double *X)
{
// works only if all 4 values in A and B are non-zero
    int i = 1 , j = 0 ; 
    if ( A[i] != 0 )
    {
        B[i] -= A[i]/A[j] * B[j];
        C[i] -= A[i]/A[j] * C[j];
        A[i] = 0 ;
    }
    if(B[i] != 0)
    {
        C[i]  = C[i] / B[i] ;
        B[i] = 1;
    }
    if(B[j] != 0)
    {
        C[j] -= C[i] * B[j];
        B[j] = 0 ; 
    }
    X[j] = C[j] / A[j];
    X[i] = C[i]; 
    
}
