#include <stdio.h>
#include <math.h>

int main() {
    // Components of the relative velocity vector
    double vx = 12.0;      // horizontal component
    double vy = -35.0;     // vertical component

    // Calculate magnitude of relative velocity vector
    double magnitude = sqrt(vx * vx + vy * vy);

    // Calculate cos(theta)
    double cos_theta = vx / magnitude;

    // Output result
    printf("cos(theta) = %.5f\n", cos_theta);
    
    return 0;
}

