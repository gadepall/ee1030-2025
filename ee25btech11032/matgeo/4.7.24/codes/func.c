double dot_prod(double *A , double *B , int m )
{
    double sum = 0.0 ; 
    for ( int i = 0 ; i < m ; i++ )
    {
        sum += A[i]*B[i] ;     
    }
    return sum; 
}



