void calc(double *P , double *U , double *X , double *Y , double r)
{
    for(int i = 0 ; i< 2 ;i++)
    {
        X[i] = P[i] + U[i]*r;
        Y[i] = P[i] - U[i]*r;
    }
}
