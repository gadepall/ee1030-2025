#include <stdio.h>
#include <math.h>

int main() {
    // Given points
    double Ax = -6, Ay = 0;
    double Cx = 3,  Cy = -8;
    double Px = -4, Py = 6;

    // Compute vectors (A - P) and (P - C)
    double APx = Ax - Px;
    double APy = Ay - Py;
    double PCx = Px - Cx;
    double PCy = Py - Cy;

    // Dot product (A - P)T(P - C)
    double dot = APx * PCx + APy * PCy;

    



    // Norm squared of (P - C)
    double norm_sq = PCx * PCx + PCy * PCy;

    // Ratio k
    double k = dot / norm_sq;

    printf("The value of k = %.3f\n", k);

    if (k > 0 && fabs(k - floor(k)) < 1e-6) {
        printf("Point P divides AC internally.\n");
    } else if (k < 0) {
        printf("Point P divides AC externally.\n");
    } else {
        printf("Point P does not divide AC.\n");
    }

    return 0;
}

