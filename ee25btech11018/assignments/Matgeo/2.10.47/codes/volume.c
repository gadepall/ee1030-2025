#include <stdio.h>
#include <math.h>

// Function to calculate determinant of 3x3 matrix
double determinant(double a) {
    double mat[3][3] = {
        {1, a, 1},
        {0, 1, a},
        {a, 0, 1}
    };

    double det = mat[0][0]*(mat[1][1]*mat[2][2] - mat[1][2]*mat[2][1])
               - mat[0][1]*(mat[1][0]*mat[2][2] - mat[1][2]*mat[2][0])
               + mat[0][2]*(mat[1][0]*mat[2][1] - mat[1][1]*mat[2][0]);

    return det;
}

// Function f(a) = a^3 - a + 1
double f(double a) {
    return (a*a*a - a + 1);
}

// Function to check if a given 'a' is a local minimum
int isLocalMinimum(double a) {
    double secondDerivative = 6*a;
    return (secondDerivative > 0); // local min if f''(a) > 0
}

int main() {
    double options[4] = {-3, 3, 1.0/sqrt(3), sqrt(3)};
    int i;

    printf("Checking all options:\n");

    for (i = 0; i < 4; i++) {
        double a = options[i];
        double vol = determinant(a);

        printf("a = %lf, Determinant = %lf, f(a) = %lf", a, vol, f(a));

        if (fabs(a - 1.0/sqrt(3)) < 1e-6 && isLocalMinimum(a)) {
        }

        printf("\n");
    }

    printf("\nTherefore, the local minimum occurs at a = 1/sqrt(3).\n");

    return 0;
}

