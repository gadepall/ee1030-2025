#include <math.h>

void get_plot_data(double* out_data) {
    double a = 2.0;
    int num_points = 51;
    double t;
    out_data[0] = a;
    out_data[1] = 0.0;

    int index = 2;
    for (int i = 0; i < num_points; i++) {
        t = -2.0 + (4.0 * i) / (num_points - 1);
        out_data[index]     = a * t * t;
        out_data[index + 1] = 2 * a * t;

        out_data[index + (num_points * 2)]     = (a + a * t * t) / 2.0;
        out_data[index + (num_points * 2) + 1] = a * t;

        index += 2;
    }
}
