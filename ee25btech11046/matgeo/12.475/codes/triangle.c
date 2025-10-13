void function(const double q[], const double p[], const double R[], double *q_new_x, double *q_new_y) {
    double temp_x = q[0] - p[0];
    double temp_y = q[1] - p[1];
    double rotated_x = R[0] * temp_x + R[1] * temp_y;
    double rotated_y = R[2] * temp_x + R[3] * temp_y;
    *q_new_x = rotated_x + p[0];
    *q_new_y = rotated_y + p[1];
}
