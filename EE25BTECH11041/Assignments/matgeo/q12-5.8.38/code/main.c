// main.c
// gcc -shared -o libsolver.so -fPIC main.c -lm

#include <stdio.h>

typedef struct {
    double A; // Alwar's age
    double D; // Daughter's age
} Solution;

// Function to solve two equations using elimination method
// Eqn1: A - 7D = -42
// Eqn2: A - 3D = 6
Solution solve_ages() {
    Solution S;

    // Coefficients:
    // eqn1: 1*A -7*D = -42
    // eqn2: 1*A -3*D = 6
    double a1 = 1, b1 = -7, c1 = -42;
    double a2 = 1, b2 = -3, c2 = 6;

    // Solve using Cramer's rule
    double det  = a1*b2 - a2*b1;
    double detA = c1*b2 - c2*b1;
    double detD = a1*c2 - a2*c1;

    S.A = detA / det;
    S.D = detD / det;

    return S;
}

#ifdef TEST_C
int main(){
    Solution S = solve_ages();
    printf("Alwar's age: %.2f\n", S.A);
    printf("Daughter's age: %.2f\n", S.D);
    return 0;
}
#endif

