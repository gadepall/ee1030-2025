#include <stdio.h>

int main() {
    double prob[7]; // Indices 1-6 for ease of use
    int v1, v2, v3;
    double result;

    // 1. Input the probabilities for sides 1 to 6
    printf("Enter the probabilities (as decimals, e.g., 0.125 for 1/8):\n");
    for (int i = 1; i <= 6; i++) {
        printf("Side %d: ", i);
        scanf("%lf", &prob[i]);
    }

    // 2. Input the three values you want to check
    printf("\nEnter the 3 values to calculate (e.g., 1 5 6): ");
    if (scanf("%d %d %d", &v1, &v2, &v3) != 3) {
        printf("Error: Please enter three integers.\n");
        return 1;
    }

    // 3. Calculation for the specific sequence (Intersection of independent events)
    // Formula: P(v1) * P(v2) * P(v3)
    result = prob[v1] * prob[v2] * prob[v3];

    printf("Probability of sequence (%d, %d, %d): %.10f\n", v1, v2, v3, result);

    return 0;
}