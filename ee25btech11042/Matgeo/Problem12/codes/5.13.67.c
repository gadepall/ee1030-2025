// solver.c

double find_k() {
    // A non-trivial solution exists if the determinant of the coefficient
    // matrix is zero. The simplified determinant equation is: -2k + 33 = 0.

    double k_coefficient = -2.0;
    double constant_term = 33.0;

    // We solve for k: k = -constant_term / k_coefficient
    double k = -constant_term / k_coefficient;

    return k;
}
