#include <math.h>

void get_tangent_data(double* out_data) {
       double tangent_x = 3.0;
    double tangent_y = 2.0;
        int num_points = 101;
    out_data[0] = tangent_x;
    out_data[1] = tangent_y;

    int index = 2;
    for (int i = 0; i < num_points; i++) {
        double x = 0.75 + (10.0 * i) / (num_points - 1);

        out_data[index]     = x;
        out_data[index + 1] = sqrt(4 * x - 3) - 1;
        index += 2;
    }
}
