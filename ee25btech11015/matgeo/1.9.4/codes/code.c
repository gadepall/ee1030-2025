#include <stdio.h>
#include <math.h>

int main() {
    float norm_a = 4;           // ||a|| = 4
    float lambda_min = -3, lambda_max = 2;

    // Compute max |lambda|
    float max_abs_lambda = fmax(fabs(lambda_min), fabs(lambda_max));
    float min_abs_lambda = 0;   // since lambda can be 0 in [-3, 2]

    // Corresponding ||lambda * a|| values
    float min_norm = norm_a * min_abs_lambda;
    float max_norm = norm_a * max_abs_lambda;

    printf("||lambda * a|| lies in [%.0f, %.0f]\n", min_norm, max_norm);

    return 0;
}