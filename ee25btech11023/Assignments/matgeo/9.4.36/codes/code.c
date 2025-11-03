#include <math.h>

void get_parabola_data(double* out_data) {
      double a = 1.0;
    double b = -4.0;
    double c = -21.0;

        double discriminant = sqrt(b*b - 4*a*c);
    double root1 = (-b + discriminant) / (2 * a);
    double root2 = (-b - discriminant) / (2 * a);
    out_data[0] = root1;
    out_data[1] = root2;
    int num_points = 101;
    out_data[2] = (double)num_points;
    int index = 3;
    for (int i = 0; i < num_points; i++) {

        double x = -5.0 + (14.0 * i) / (num_points - 1);
        double y = a*x*x + b*x + c;

        out_data[index] = x;
        out_data[index + 1] = y;
        index += 2;
    }
}
