#include <stdio.h>
#include <math.h>

// Function to solve for eigenvalues and eigenvectors of the given 3x3 matrix
// Results: eigenvalues[3], eigenvectors[9] (flattened column-major)
void solve_eigen(double *eigenvalues, double *eigenvectors) {
    // Eigenvalues known from block diagonal argument
    eigenvalues[0] = 3.0;
    eigenvalues[1] = 8.0;
    eigenvalues[2] = 4.0;

    // Corresponding orthonormal eigenvectors
    // v1 = (1,0,0)
    eigenvectors[0] = 1.0; eigenvectors[1] = 0.0; eigenvectors[2] = 0.0;

    // v2 = (0,1,1)/sqrt(2)
    eigenvectors[3] = 0.0; eigenvectors[4] = 1.0/sqrt(2.0); eigenvectors[5] = 1.0/sqrt(2.0);

    // v3 = (0,1,-1)/sqrt(2)
    eigenvectors[6] = 0.0; eigenvectors[7] = 1.0/sqrt(2.0); eigenvectors[8] = -1.0/sqrt(2.0);
}


