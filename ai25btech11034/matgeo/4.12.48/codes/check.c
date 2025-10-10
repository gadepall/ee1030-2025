#include <stdio.h>
#include <math.h>

// Function to check condition: 1/a^2 + 1/b^2 + 1/c^2 == 1/p^2
int check_condition(double a, double b, double c, double p) {
    double lhs = 1.0/(a*a) + 1.0/(b*b) + 1.0/(c*c);
    double rhs = 1.0/(p*p);

    if (fabs(lhs - rhs) < 1e-6) {
        return 1;  // condition satisfied
    } else {
        return 0;  // not satisfied
    }
}

