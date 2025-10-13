#include <stdio.h>

int main() {
    // --- Given Problem Data ---
    // The point (x1, y1) on the curve 2y + x^2 = 3.
    double x1 = 1.0;
    double y1 = 1.0;

    // --- Calculations ---
    // 1. Find the slope of the tangent from the derivative dy/dx = -x.
    double m_tangent = -x1;

    // A horizontal tangent (slope=0) means the normal is a vertical line.
    if (m_tangent == 0) {
        printf("The equation of the normal line is: x = %.2f\n", x1);
    } else {
        // 2. The slope of the normal is the negative reciprocal.
        double m_normal = -1.0 / m_tangent;

        // 3. The y-intercept 'c' is calculated from y = mx + c.
        double c = y1 - m_normal * x1;

        // --- Print the Final Answer ---
        // This logic helps format the equation cleanly (e.g., printing "y = x"
        // instead of "y = 1.00x + 0.00").
        printf("The equation of the normal line is: ");

        if (m_normal == 1 && c == 0) {
            printf("y = x\n");
        } else if (m_normal == -1 && c == 0) {
            printf("y = -x\n");
        } else {
            printf("y = %.2fx", m_normal);
            if (c > 0) {
                printf(" + %.2f\n", c);
            } else if (c < 0) {
                printf(" - %.2f\n", -c);
            } else {
                printf("\n");
            }
        }
    }
    return 0;
}