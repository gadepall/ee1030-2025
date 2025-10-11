#include <stdio.h>

// Compute slope of required line
double compute_slope() {
    // Given line: x + y + 1 = 0 → slope = -1
    double slope_given = -1.0;

    // Required line ⟂ given line → slope = -1 / slope_given
    double slope_required = -1.0 / slope_given;

    return slope_required;  // should be 1.0
}

