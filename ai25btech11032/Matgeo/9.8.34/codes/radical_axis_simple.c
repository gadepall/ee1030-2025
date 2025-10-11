// Compute radical axis of two circles in conic form
// Circle: x^T V x + 2u^T x + f = 0 with V = a I
// Input: a1,u1,f1 and a2,u2,f2
// Output: line L^T x + c = 0 (L is size 2, c scalar)

void radical_axis(
    double a1, const double u1[2], double f1,
    double a2, const double u2[2], double f2,
    double L_out[2], double *c_out
) {
    double mu = -a1 / a2; // value that cancels quadratic part
    L_out[0] = 2.0 * (u1[0] + mu * u2[0]);
    L_out[1] = 2.0 * (u1[1] + mu * u2[1]);
    *c_out    =       (f1     + mu * f2);
}

