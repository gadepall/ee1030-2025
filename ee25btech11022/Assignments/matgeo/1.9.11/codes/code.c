#include <stdio.h>
#include <math.h>

// Fills k and both point arrays.
void find_k_and_points(double *k, double pt1[2], double pt2[2]) {
    *k = 3 + sqrt(84);
    pt1[0] = *k;  pt1[1] = -2;
    pt2[0] = 3;   pt2[1] = -6;
}

int main() {
    double k, pt1[2], pt2[2];
    find_k_and_points(&k, pt1, pt2);
    printf("Positive value of k: %.6f\n", k);
    printf("First point: (%.6f, %.6f)\n", pt1[0], pt1[1]);
    printf("Second point: (%.6f, %.6f)\n", pt2[0], pt2[1]);
    return 0;
}

