#include <stdio.h>

void sectionFormula(int m, int n, float P[2], float Q[2], float R[2]) {
    for (int i = 0; i < 2; i++) {
        R[i] = (m * Q[i] + n * P[i]) / (float)(m + n);
    }
}
