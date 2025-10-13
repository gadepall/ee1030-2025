#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Create matrix function
double **createMat(int m, int n)
{
    int i;
    double **a;
    a = (double **)malloc(m * sizeof(*a));
    for (i = 0; i < m; i++)
        a[i] = (double *)malloc(n * sizeof(*a[i]));
    return a;
}

// Matrix multiplication (for Matdot)
double **transposeMat(double **a, int m, int n);
double **Matmul(double **a, double **b, int m, int n, int p);
double Matdot(double **a, double **b, int m);
double Matnorm(double **a, int m);

// Definitions for these matrix helper functions

double **transposeMat(double **a, int m, int n)
{
    int i, j;
    double **c = createMat(n, m);
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            c[i][j] = a[j][i];
    return c;
}

double **Matmul(double **a, double **b, int m, int n, int p)
{
    int i, j, k;
    double **c = createMat(m, p);
    for (i = 0; i < m; i++)
    {
        for (k = 0; k < p; k++)
        {
            double temp = 0;
            for (j = 0; j < n; j++)
            {
                temp += a[i][j] * b[j][k];
            }
            c[i][k] = temp;
        }
    }
    return c;
}

double Matdot(double **a, double **b, int m)
{
    double **temp = Matmul(transposeMat(a, m, 1), b, 1, m, 1);
    double val = temp[0][0];
    // Free temp for good practice
    for (int i = 0; i < 1; i++) free(temp[i]);
    free(temp);
    return val;
}

double Matnorm(double **a, int m)
{
    return sqrt(Matdot(a, a, m));
}

// Solve lambda values given vectors n and P (both m x 1)
void solve_lambda(double **n, double **P, double d, double *lambda_out)
{
    int m = 3;
    double n_dot_P = Matdot(n, P, m);
    double n_norm = Matnorm(n, m);
    lambda_out[0] = d * n_norm - n_dot_P;
    lambda_out[1] = -d * n_norm - n_dot_P;
}

// Example main for testing (optional)
/*
int main() {
    int m = 3, n = 1;
    double **n_vec = createMat(m, n);
    double **P = createMat(m, n);
    double d = 5.0 / sqrt(3.0);
    double lambda_out[2];

    n_vec[0][0] = 1.0; n_vec[1][0] = -1.0; n_vec[2][0] = 1.0;
    P[0][0] = 1.0; P[1][0] = 1.0; P[2][0] = 1.0;

    solve_lambda(n_vec, P, d, lambda_out);

    printf("Possible values of lambda: %lf, %lf\n", lambda_out[0], lambda_out[1]);

    for (int i = 0; i < m; i++) {
        free(n_vec[i]);
        free(P[i]);
    }
    free(n_vec);
    free(P);

    return 0;
}
*/
