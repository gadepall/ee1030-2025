#include <math.h>
void function(const double x_coords[], int num_points, double* y_out) {
    for (int i = 0; i < num_points; i++) {
        double x = x_coords[i];
        y_out[i] = (x * x + 5.0) / 10.0;
    }
}
