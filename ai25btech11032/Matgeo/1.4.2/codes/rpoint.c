/* rpoint.c — pure C, 2D only */
void point_on_segment2d(const double P[2], const double Q[2], double lambda, double R[2]) {
    R[0] = P[0] + lambda * (Q[0] - P[0]);
    R[1] = P[1] + lambda * (Q[1] - P[1]);
}
