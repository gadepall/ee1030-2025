#include <stdio.h>

void solve_car_speeds(double distance, double time_same_dir, double time_towards, double *v1, double *v2) {
    double sum_speeds = distance / time_towards;
    double diff_speeds = distance / time_same_dir;

    *v1 = (sum_speeds + diff_speeds) / 2.0;
    *v2 = sum_speeds - *v1;
}
