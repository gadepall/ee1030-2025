#include <stdio.h>

// Function to compute determinant of 3x3 matrix
double determinant(double a[3][3]) {
    return a[0][0]*(a[1][1]*a[2][2] - a[1][2]*a[2][1])
         - a[0][1]*(a[1][0]*a[2][2] - a[1][2]*a[2][0])
         + a[0][2]*(a[1][0]*a[2][1] - a[1][1]*a[2][0]);
}

int main() {
    double lambda;
    double A[3][3];
    double det;
    int count = 0;
    double roots[10]; // to store λ values
    
    printf("Finding λ for which system has non-trivial solutions...\n");

    // Scan integer λ values from -10 to 10
    for (lambda = -10; lambda <= 10; lambda++) {
        A[0][0] = 2 - lambda;  A[0][1] = -2;       A[0][2] = 1;
        A[1][0] = 2;           A[1][1] = -3 - lambda; A[1][2] = 2;
        A[2][0] = -1;          A[2][1] = 2;        A[2][2] = -lambda;

        det = determinant(A);

        if (det == 0) {
            roots[count++] = lambda;
        }
    }

    printf("Number of λ values found: %d\n", count);
    for (int i = 0; i < count; i++) {
        printf("λ = %.2f\n", roots[i]);
    }

    if (count == 2)
        printf("Correct Answer: (A) contains two elements\n");
    else if (count > 2)
        printf("Option (B)\n");
    else if (count == 0)
        printf("Option (C)\n");
    else
        printf("Option (D)\n");

    return 0;
}
