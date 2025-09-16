#include <stdio.h>
#include <math.h>

// Function to solve the locus equation for k=10
void solveSphere() {
    double k = 10.0;

    // Center of sphere (from derivation)
    double Cx = 1.0;
    double Cy = 7.0 / 2.0;  // 3.5
    double Cz = -1.0;

    // Radius squared (correct formula)
    double R2 = k * k - 161.0 / 4.0;  // 100 - 40.25 = 59.75

    if (R2 <= 0) {
        printf("For k = %.2f, no real sphere exists (radius^2 = %.2f)\n", k, R2);
        return;
    }

    double R = sqrt(R2);

    printf("Equation of the sphere:\n");
    printf("(x - %.2f)^2 + (y - %.2f)^2 + (z - %.2f)^2 = %.2f\n", 
           Cx, Cy, Cz, R * R);

    printf("Center: (%.2f, %.2f, %.2f)\n", Cx, Cy, Cz);
    printf("Radius: %.2f\n", R);
}

int main() {
    solveSphere();  // for k=10
    return 0;
}
