#include <math.h>


void find_k_values(double* k_pos, double* k_neg) {
    // Area = 0.5 * |k| * |k/5| = 5  =>  k^2 = 50
    *k_pos = sqrt(50.0);
    *k_neg = -sqrt(50.0);
}
