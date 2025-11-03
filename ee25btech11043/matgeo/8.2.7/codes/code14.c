#include <math.h>

// Function to calculate ellipse properties and pass them back via pointers
void calculateEllipseProperties(
    double a_val,
    double b_val,
    double* focus_y_ptr,
    double* vertex_y_ptr,
    double* eccentricity_ptr,
    double* directrix_y_ptr,
    double* latus_rectum_ptr
) {
    double c_val = sqrt(a_val * a_val - b_val * b_val);

    *focus_y_ptr = c_val;
    *vertex_y_ptr = a_val;
    *eccentricity_ptr = c_val / a_val;
    *directrix_y_ptr = a_val / (*eccentricity_ptr); // Use the calculated eccentricity
    *latus_rectum_ptr = (2 * b_val * b_val) / a_val;
}