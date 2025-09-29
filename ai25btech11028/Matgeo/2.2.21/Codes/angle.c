#include <stdio.h>
#include <math.h>

// Function to find slopes of second line given m1 and angle
int find_other_slopes(double m1, double theta, double *slopes) {
    // Equation derived: tan(theta) = |(m2 - m1) / (1 + m1*m2)|
    // Rearranged: (m2 - m1) = ± tan(theta) * (1 + m1*m2)

    double t = tan(theta);

 // Case 1: (m2 - m1) = +t(1 + m1*m2)
    // => m2 - t*m1*m2 = m1 + t
    // => m2(1 - t*m1) = m1 + t
    slopes[0] = (m1 + t) / (1 - t*m1);

    // Case 2: (m2 - m1) = -t(1 + m1*m2)
    // => m2 + t*m1*m2 = m1 - t
    // => m2(1 + t*m1) = m1 - t
    slopes[1] = (m1 - t) / (1 + t*m1);

    return 2;  // number of solutions
    }