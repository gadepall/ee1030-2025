#include <stdio.h>
#include <math.h>

int main() {
    double total_area, half_area, a, lhs;

    // Step 1: Find total area between x = y^2 and x = 4
    // Limits are y = -2 to y = 2
    total_area = (4*2 - pow(2,3)/3) - (4*(-2) - pow(-2,3)/3);
    // Simplify the above: total_area = 32/3
    printf("Total area between x = y^2 and x = 4 : %.6lf\n", total_area);

    // Step 2: Half of the total area
    half_area = total_area / 2.0;
    printf("Half of total area : %.6lf\n", half_area);

    // Step 3: For x = a dividing the region into equal parts:
    // Area between x = y^2 and x = a is (4/3) * a^(3/2)
    // We set (4/3)*a^(3/2) = half_area
    // => a^(3/2) = (3/4)*half_area
    double rhs = (3.0/4.0) * half_area;

    // Now find a = (rhs)^(2/3)
    a = pow(rhs, 2.0/3.0);

    // Step 4: Display results
    printf("Equation used: (4/3)*a^(3/2) = %.6lf\n", half_area);
    printf("=> a^(3/2) = %.6lf\n", rhs);
    printf("=> a = (%.6lf)^(2/3)\n", rhs);
    printf("Value of a = %.6lf\n", a);

    return 0;
}

