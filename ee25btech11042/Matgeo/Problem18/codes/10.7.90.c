#include <math.h>
#include <stdio.h>

// This function calculates the properties of the circle based on the problem's geometric constraints.
// It iterates through possible centers and uses the interior point condition to find the unique solution.
void find_circle_properties(double center[2], double *radius) {
    // From the problem statement:
    // r^2 = 50.0 is derived from the chord and tangent line geometry.
    // The four potential centers are (9,-1), (-1,9), (1,-9), (-9,1).
    // The interior point is Q(-10, 2).

    double r_squared = 50.0;
    double Q[] = {-10.0, 2.0};
    
    double possible_centers[4][2] = {
        {9.0, -1.0},
        {-1.0, 9.0},
        {1.0, -9.0},
        {-9.0, 1.0}
    };

    // Check each potential center to see if Q is an interior point.
    // A point Q is inside a circle with center C and radius r if ||Q - C||^2 < r^2.
    for (int i = 0; i < 4; ++i) {
        double C[2] = {possible_centers[i][0], possible_centers[i][1]};
        double dist_sq = pow(Q[0] - C[0], 2) + pow(Q[1] - C[1], 2);
        
        if (dist_sq < r_squared) {
            // This is the correct center.
            center[0] = C[0];
            center[1] = C[1];
            *radius = sqrt(r_squared);
            return;
        }
    }
}
