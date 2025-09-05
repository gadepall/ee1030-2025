#include <stdio.h>
#include <math.h>

int main() {
    double lambda1, lambda2;

    // Equation: (λ + 6) / sqrt((λ+2)^2 + 40) = 1
    // Square both sides => (λ+6)^2 = (λ+2)^2 + 40

    // Expanding manually:
    // λ^2 + 12λ + 36 = λ^2 + 4λ + 44
    // => 8λ = 8
    // => λ = 1

    lambda1 = 1;

    printf("The value of lambda is: %.2f\n", lambda1);

    return 0;
}