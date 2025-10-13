#include <stdio.h>
#include <math.h>

void row_mal(double X[][3] , double k , int n , int m)
{
    for(int i = 0 ; i< 3 ; i++)
    {
        X[n][i] = X[n][i] - k * X[m][i];
    }
}

void row_div(double X[][3] , double k , int n )
{
    for(int i = 0 ; i< 3 ; i++)
    {
        X[n][i] /= k ;
    }
}

void augment(double *A , double *B , double *C)
{
    double X[2][3];
    for(int i = 0; i< 2 ; i++)
    {
        X[i][0] = A[i];
        X[i][1] = B[i];
        X[i][2] = C[i];
    }

    if(X[0][0] != 0 )
    {
        row_div(X,X[0][0],0);
        if(X[1][0] != 0)
        {
            row_mal(X,X[1][0],1,0);
        }
    }
    else
    {
        row_mal(X,-1,0,1);
        row_div(X,X[0][0],0);
        if(X[1][0] != 0)
        {
            row_mal(X,X[1][0],1,0);
        }
    }
    
    if(X[1][1] != 0 )
    {
        row_div(X,X[1][1],1);
        if(X[0][1] != 0)
        {
            row_mal(X,X[0][1],0,1);
        }
    }
    else
    {
        row_mal(X,-1,1,0);
        row_div(X,X[1][1],1);
        if(X[0][1] != 0)
        {
            row_mal(X,X[0][1],0,1);
        }

    }

    for(int i = 0 ; i< 2 ; i++)
    {
        C[i] = 1 / X[i][2] ;
        for(int j = 0; j < 3; j++)
        {
            printf("%.3f ",X[i][j]);
        }
        printf("\n");
    }

            
}



