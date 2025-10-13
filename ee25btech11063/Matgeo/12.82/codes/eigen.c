#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define N 3
#define MAX_ITERS 100
#define EPS 1e-12

/* Find largest off-diagonal element (absolute) and return its indices i,j */
void max_offdiag(double A[N][N], int *pi, int *pj) {
    double max = 0.0;
    int imax = 0, jmax = 1;
    for (int i = 0; i < N; ++i) {
        for (int j = i+1; j < N; ++j) {
            double v = fabs(A[i][j]);
            if (v > max) {
                max = v;
                imax = i; jmax = j;
            }
        }
    }
    *pi = imax; *pj = jmax;
}

/* Perform Jacobi rotations to diagonalize symmetric 3x3 matrix A in-place.
   On return, A will be near-diagonal and diagonal entries approximate eigenvalues. */
void jacobi_eigensolver(double A[N][N], double eig[N]) {
    double V[N][N] = {0}; // eigenvector matrix (not used for result but kept)
    for (int i=0;i<N;i++) V[i][i]=1.0;

    double B[N][N];
    for (int i=0;i<N;i++)
        for (int j=0;j<N;j++)
            B[i][j]=A[i][j];

    for (int iter = 0; iter < MAX_ITERS; ++iter) {
        int p,q;
        max_offdiag(B, &p, &q);
        double bpq = B[p][q];
        if (fabs(bpq) < EPS) break;

        double app = B[p][p];
        double aqq = B[q][q];

        double tau = (aqq - app) / (2.0 * bpq);
        double t;
        if (tau >= 0.0) t = 1.0 / (tau + sqrt(1.0 + tau*tau));
        else t = -1.0 / (-tau + sqrt(1.0 + tau*tau));
        double c = 1.0 / sqrt(1.0 + t*t);
        double s = t * c;
        double tauPrime = s/(1.0 + c);

        // update matrix B
        double app_new = app - t * bpq;
        double aqq_new = aqq + t * bpq;
        B[p][p] = app_new;
        B[q][q] = aqq_new;
        B[p][q] = B[q][p] = 0.0;

        for (int k = 0; k < N; ++k) {
            if (k != p && k != q) {
                double bkp = B[k][p];
                double bkq = B[k][q];
                B[k][p] = B[p][k] = bkp - s*(bkq + tauPrime*bkp);
                B[k][q] = B[q][k] = bkq + s*(bkp - tauPrime*bkq);
            }
        }

        // (optional) update eigenvector matrix V if needed
        for (int k = 0; k < N; ++k) {
            double vkp = V[k][p];
            double vkq = V[k][q];
            V[k][p] = vkp - s*(vkq + tauPrime*vkp);
            V[k][q] = vkq + s*(vkp - tauPrime*vkq);
        }
    }

    // diagonal entries are eigenvalue approximations
    for (int i = 0; i < N; ++i) eig[i] = B[i][i];
}

/* Example: you may replace the M matrix below with whichever symmetric 3x3 matrix you want */
int main(void) {
    /* Example symmetric matrix M.
       If you expect eigenvalues 1,2,3 for M, use a matrix with those eigenvalues (e.g. diag(1,2,3),
       or Q*diag(1,2,3)*Q^T for some orthogonal Q). */
    double M[N][N] = {
        {1.0, 0.0, 0.0},
        {0.0, 2.0, 0.0},
        {0.0, 0.0, 3.0}
    };

    /* --- If you want a different M, edit the matrix above. --- */

    double lambda[N];
    jacobi_eigensolver(M, lambda);

    /* Jacobi may produce eigenvalues in any order; we trust them as computed.
       Compute mu_i = 3/(2*lambda_i). Guard against tiny/zero eigenvalue. */
    double mu[N];
    for (int i = 0; i < N; ++i) {
        if (fabs(lambda[i]) < 1e-14) {
            fprintf(stderr, "Eigenvalue near zero; cannot compute mu = 3/(2*lambda).\n");
            return 1;
        }
        mu[i] = 3.0 / (2.0 * lambda[i]);
    }

    FILE *fp = fopen("eigen.dat", "w");
    if (!fp) {
        perror("fopen");
        return 1;
    }

    /* Write only the three eigenvalues of N, one per line */
    for (int i = 0; i < N; ++i) {
        fprintf(fp, "%.12g\n", mu[i]);
    }
    fclose(fp);

    /* Informative message to stdout */
    printf("Wrote 3 eigenvalues of N to eigen.dat\n");
    return 0;
}

