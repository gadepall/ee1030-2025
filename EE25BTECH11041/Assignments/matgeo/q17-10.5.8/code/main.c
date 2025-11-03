// main.c
#include <stdio.h>
#include <math.h>

// Function to calculate tangent length between two concentric circles
// Formula: PT = sqrt(R^2 - r^2)
double tangent_length(double R, double r) {
    if (R <= r) {
        printf("Invalid input: Outer radius must be greater than inner radius.\n");
        return -1;
    }
    return sqrt((R * R) - (r * r));
}

