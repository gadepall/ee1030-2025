#include <stdio.h>
#include <complex.h>
#include <math.h>

#define MAX_DEGREE 10
#define ITERATIONS 1000

// Function to evaluate polynomial at a complex point x
double complex evaluate(double coeff[], int degree, double complex x) {
    double complex res = coeff[degree];
    for (int i = degree - 1; i >= 0; i--) {
        res = res * x + coeff[i];
    }
    return res;
}

// Root finding using Durand-Kerner algorithm
void find_roots(double coeff[], int degree, double complex roots[]) {
    if (degree == 0) return;
    
    // Initial guesses for roots (complex numbers on a circle)
    for (int i = 0; i < degree; i++) {
        roots[i] = cpow(0.4 + 0.9 * I, i);
    }

    for (int iter = 0; iter < ITERATIONS; iter++) {
        for (int i = 0; i < degree; i++) {
            double complex denom = 1.0;
            for (int j = 0; j < degree; j++) {
                if (i != j) denom *= (roots[i] - roots[j]);
            }
            roots[i] -= evaluate(coeff, degree, roots[i]) / (coeff[degree] * denom);
        }
    }
}

int main() {
    int n_deg, d_deg;
    double num[MAX_DEGREE], den[MAX_DEGREE];
    double complex zeros[MAX_DEGREE], poles[MAX_DEGREE];

    printf("Enter degree of Numerator: ");
    scanf("%d", &n_deg);
    printf("Enter coefficients (from constant to highest power):\n");
    for(int i = 0; i <= n_deg; i++) scanf("%le", &num[i]);

    printf("\nEnter degree of Denominator: ");
    scanf("%d", &d_deg);
    printf("Enter coefficients (from constant to highest power):\n");
    for(int i = 0; i <= d_deg; i++) scanf("%le", &den[i]);

    find_roots(num, n_deg, zeros);
    find_roots(den, d_deg, poles);

    printf("TYPE,REAL,IMAG\n");
    for(int i = 0; i < n_deg; i++) 
        printf("ZERO,%.5f,%.5f\n", creal(zeros[i]), cimag(zeros[i]));
    for(int i = 0; i < d_deg; i++) 
        printf("POLE,%.5f,%.5f\n", creal(poles[i]), cimag(poles[i]));

    return 0;
}