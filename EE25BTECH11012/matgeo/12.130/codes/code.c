#include <stdio.h>
#include <math.h>
#include <complex.h>

int main() {
    // b = (0, 1, 0)
    // Cross product matrix M for b × x is:
    // |  0   0   1 |
    // |  0   0   0 |
    // | -1   0   0 |

    double M[3][3] = {
        {0, 0, 1},
        {0, 0, 0},
        {-1, 0, 0}
    };

    // Characteristic equation of M:
    // |M - λI| = 0 gives  λ(λ^2 + 1) = 0
    // ⇒ λ = 0, i, -i

    double complex eigen1 = 0.0 + 0.0 * I;
    double complex eigen2 = 0.0 + 1.0 * I;
    double complex eigen3 = 0.0 - 1.0 * I;

    printf("The eigenvalues of matrix M are:\n");
    printf("λ1 = %.1f + %.1fi\n", creal(eigen1), cimag(eigen1));
    printf("λ2 = %.1f + %.1fi\n", creal(eigen2), cimag(eigen2));
    printf("λ3 = %.1f + %.1fi\n", creal(eigen3), cimag(eigen3));
    return 0;
}