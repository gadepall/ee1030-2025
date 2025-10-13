#include <stdio.h>
#include <math.h>

// Function to check the condition for circle chords
double check_condition(double p, double q) {
    // If chords from (p,q) are bisected by x-axis,
    // then p^2 = 8q^2 must hold.
    return p*p - 8*q*q;
}

int main() {
    double p, q;
    printf("Enter p and q: ");
    scanf("%lf %lf", &p, &q);

    double result = check_condition(p, q);

    if (fabs(result) < 1e-6)
        printf("Condition satisfied: p^2 = 8q^2\n");
    else if (result > 0)
        printf("p^2 > 8q^2\n");
    else
        printf("p^2 < 8q^2\n");

    return 0;
}