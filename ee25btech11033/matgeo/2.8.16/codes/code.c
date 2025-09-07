#include <stdio.h>

int is_perpendicular(double p, double r, double p_prime, double r_prime) {
    if ((p * p_prime) + (r * r_prime) + 1 == 0) {
        return 1; // True, the lines are perpendicular
    }
    return 0; // False, the lines are not perpendicular
}