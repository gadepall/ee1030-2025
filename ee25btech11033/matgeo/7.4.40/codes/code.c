#include <math.h> // For sqrt()

/* Define a structure to hold all the calculated points.
  This makes it easy to pass all the data back to Python.
*/
struct PlotData {
    double center_x, center_y;
    double radius;
    double P_x, P_y;
    double M1_x, M1_y;
    double M2_x, M2_y;
    double Q1_x, Q1_y;
    double Q2_x, Q2_y;
};

/* A helper function to solve the quadratic equation Ax^2 + Bx + C = 0.
  It stores the two roots in the pointers root1 and root2.
*/
void solve_quadratic(double A, double B, double C, double *root1, double *root2) {
    // We assume real roots based on the problem's geometry
    double discriminant = B*B - 4*A*C;
    double sqrt_discriminant = sqrt(discriminant); 
    
    *root1 = (-B + sqrt_discriminant) / (2.0 * A);
    *root2 = (-B - sqrt_discriminant) / (2.0 * A);
}

/* The main function to be exported from the library.
  It is now a standard C function declaration.
*/
void calculate_plot_values(double a, double b, struct PlotData *data) {
    // --- Circle Properties ---
    data->center_x = a / 2.0;
    data->center_y = b / 4.0;
    data->radius = sqrt(a*a/4.0 + b*b/16.0);

    // --- External Point ---
    data->P_x = a;
    data->P_y = b / 2.0;

    // --- Find Chord Midpoints (M1, M2) ---
    // Roots of 8h^2 - 12ah + (4a^2 + b^2) = 0
    double A_h = 8.0;
    double B_h = -12.0 * a;
    double C_h = 4.0*a*a + b*b;
    solve_quadratic(A_h, B_h, C_h, &(data->M1_x), &(data->M2_x));
    data->M1_y = 0.0;
    data->M2_y = 0.0;

    // --- Find Chord Endpoints (Q1, Q2) ---
    // Roots of 2x^2 - 2ax + b^2 = 0
    double A_x = 2.0;
    double B_x = -2.0 * a;
    double C_x = b * b;
    solve_quadratic(A_x, B_x, C_x, &(data->Q1_x), &(data->Q2_x));
    // From the original script, both Q1 and Q2 have y = -b/2
    data->Q1_y = -b / 2.0;
    data->Q2_y = -b / 2.0;
}
