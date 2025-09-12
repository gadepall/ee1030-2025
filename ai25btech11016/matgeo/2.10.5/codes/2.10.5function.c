// orthocenter.c
#include <stdio.h>

// Function to compute orthocenter of triangle ABC
// A, B, C are arrays of length 2: [x, y]
// D is output array of length 2: [x, y]
void orthocenter(double *A, double *B, double *C, double *D) {
    // Slopes of sides
    double m_BC = (C[1] - B[1]) / (C[0] - B[0]);
    double m_AC = (C[1] - A[1]) / (C[0] - A[0]);

    // Slopes of altitudes (negative reciprocal)
    double m_alt_A = -1.0 / m_BC;
    double m_alt_B = -1.0 / m_AC;

    // Equation of altitude from A: y - A_y = m_alt_A(x - A_x)
    // Equation of altitude from B: y - B_y = m_alt_B(x - B_x)

    double x_num = (m_alt_A*A[0] - m_alt_B*B[0] + B[1] - A[1]);
    double x_den = (m_alt_A - m_alt_B);
    double x = x_num / x_den;
    double y = m_alt_A*(x - A[0]) + A[1];

    D[0] = x;
    D[1] = y;
}
