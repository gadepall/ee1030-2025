double calc(double *A, int m ,int n)
{
    //double A[] = {1.0,1.0,-1.0};
    //int m = 3;
    double M[2*m-1][m];
    int t = 0 ; 
    for(int j = 0 ; j < m  ; j++)
    {
        int k = 0 ;
        
        for(int i = t ; i < t+m ; i++ )
        {
            M[i][j] = A[k];
            k++;
        }
        
        if(t == m-1 )
        {
            break;
        }
        t++;
    }
    
    double ans = 0 ; 
    for(int i = 0 ; i < m ; i++)
    {
        ans += A[i] * M[n][i];
    }
    return ans;

}
