
#include <stdio.h>
#include <math.h>

#define N 3

void compute_X(double X[N][N]) {
    for (int i=0; i<N; ++i)
        for (int j=0; j<N; ++j)
            X[i][j] = (i==j) ? 6.0 : 12.0;
}

double trace(double X[N][N]) {
    double t = 0.0;
    for (int i=0; i<N; ++i)
        t += X[i][i];
    return t;
}

int is_symmetric(double X[N][N], double tol) {
    for (int i=0; i<N; ++i)
        for (int j=i+1; j<N; ++j)
            if (fabs(X[i][j]-X[j][i])>tol)
                return 0;
    return 1;
}

void mat_vec_mul(double X[N][N], double v[N], double y[N]) {
    for (int i=0; i<N; ++i){
        y[i]=0;
        for (int j=0; j<N; ++j)
            y[i]+=X[i][j]*v[j];
    }
}

void subtract_scalar_I(double X[N][N], double scalar, double Y[N][N]) {
    for (int i=0;i<N;++i)
        for (int j=0;j<N;++j)
            Y[i][j] = X[i][j] - (i==j ? scalar : 0);
}

double determinant(double X[N][N]) {
    return X[0][0]*(X[1][1]*X[2][2]-X[1][2]*X[2][1])
         - X[0][1]*(X[1][0]*X[2][2]-X[1][2]*X[2][0])
         + X[0][2]*(X[1][0]*X[2][1]-X[1][1]*X[2][0]);
}

