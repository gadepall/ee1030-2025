#include <stdio.h>
#include <math.h>

int main() {
    FILE *fp;
    fp = fopen("eigen.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Matrix A
    // A = [[5, 3],
    //      [1, 3]]

    // Eigenvalues are already known: λ1=6, λ2=2
    // We’ll compute the corresponding eigenvectors.

    // Eigenvector for λ1 = 6  --> [3, 1]
    double v1x = 3, v1y = 1;
    double norm1 = sqrt(v1x*v1x + v1y*v1y);
    v1x /= norm1;
    v1y /= norm1;

    // Eigenvector for λ2 = 2  --> [1, -1]
    double v2x = 1, v2y = -1;
    double norm2 = sqrt(v2x*v2x + v2y*v2y);
    v2x /= norm2;
    v2y /= norm2;

    // Write to file
    fprintf(fp, "Normalized Eigenvectors:\n");
    fprintf(fp, "For λ1 = 6 : ( %.6f , %.6f )\n", v1x, v1y);
    fprintf(fp, "For λ2 = 2 : ( %.6f , %.6f )\n", v2x, v2y);

    fclose(fp);

    printf("Eigenvectors written to eigen.dat\n");
    return 0;
}

