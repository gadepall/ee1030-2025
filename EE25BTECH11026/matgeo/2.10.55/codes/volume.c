#include <stdio.h>
#include <math.h>

// Jacobi eigenvalue algorithm for 3x3 symmetric matrix
// Finds eigenvalues of G
void jacobi_eigenvalues(double G[3][3], double eigenvalues[3]) {
    double A[3][3];
    for(int i=0;i<3;i++) {
        for(int j=0;j<3;j++) A[i][j] = G[i][j];
    }

    double eps = 1e-12;
    for(int iter=0; iter<100; iter++) {
        // find largest off-diagonal element
        int p=0,q=1;
        double max = fabs(A[0][1]);
        for(int i=0;i<3;i++) {
            for(int j=i+1;j<3;j++) {
                if(fabs(A[i][j]) > max) { max=fabs(A[i][j]); p=i; q=j; }
            }
        }
        if(max < eps) break;

        double theta = 0.5 * atan2(2*A[p][q], A[q][q]-A[p][p]);
        double c = cos(theta), s = sin(theta);

        // rotate
        double app = c*c*A[p][p] - 2*s*c*A[p][q] + s*s*A[q][q];
        double aqq = s*s*A[p][p] + 2*s*c*A[p][q] + c*c*A[q][q];
        A[p][q] = A[q][p] = 0.0;
        A[p][p] = app;
        A[q][q] = aqq;

        for(int k=0;k<3;k++) {
            if(k!=p && k!=q) {
                double akp = c*A[k][p] - s*A[k][q];
                double akq = s*A[k][p] + c*A[k][q];
                A[k][p] = A[p][k] = akp;
                A[k][q] = A[q][k] = akq;
            }
        }
    }

    // diagonal entries are eigenvalues
    for(int i=0;i<3;i++) eigenvalues[i] = A[i][i];
}

// Volume from eigenvalues
double parallelepiped_volume(double G[3][3]) {
    double eigenvalues[3];
    jacobi_eigenvalues(G, eigenvalues);

    double det = eigenvalues[0] * eigenvalues[1] * eigenvalues[2];
    if(det < 0) det = -det;
    return sqrt(det);
}

