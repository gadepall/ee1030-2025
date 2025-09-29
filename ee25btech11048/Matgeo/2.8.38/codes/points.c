#include <math.h>
#include <stdio.h>

// Function to compute direction cosine k
// Returns positive root; negative handled in Python
double compute_k() {
    double k = 1.0 / sqrt(3.0);
    return k;
}


int main() {
    double k = compute_k();
    printf("k = %lf\n", k);
    printf("-k = %lf\n", -k);
    return 0;
}


