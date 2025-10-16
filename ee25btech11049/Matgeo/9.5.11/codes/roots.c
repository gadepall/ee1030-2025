#include <math.h>

/*
 * Calculates the real roots of a standard quadratic equation ax^2 + bx + c = 0.
 * Kept for reference.
 */
void solve_quadratic(double a, double b, double c, double* root1, double* root2) {
    double discriminant = b*b - 4*a*c;
    if (discriminant >= 0) {
        *root1 = (-b + sqrt(discriminant)) / (2 * a);
        *root2 = (-b - sqrt(discriminant)) / (2 * a);
    } else {
        *root1 = NAN;
        *root2 = NAN;
    }
}

/*
 * Calculates the intersection parameter 'kappa' for a line and a conic.
 * The conic is defined by x'Vx + 2u'x + f = 0.
 * The line is defined by x = h + kappa*m.
 * V is a 2x2 matrix (passed as a flat array [V11, V12, V21, V22]).
 * u, h, m are 2x1 vectors (passed as flat arrays).
 */
void solve_conic_intersection(double* V, double* u, double f, double* h, double* m, double* kappa1, double* kappa2) {
    // Unpack vectors for clarity
    double h1 = h[0], h2 = h[1];
    double m1 = m[0], m2 = m[1];
    double u1 = u[0], u2 = u[1];

    // Unpack matrix (assuming row-major: V[0]=V11, V[1]=V12, V[2]=V21, V[3]=V22)
    double V11 = V[0], V12 = V[1], V21 = V[2], V22 = V[3];

    // 1. Calculate m_T_V_m
    double m_T_V_m = m1*(V11*m1 + V12*m2) + m2*(V21*m1 + V22*m2);

    // 2. Calculate g(h) = h'Vh + 2u'h + f
    double h_T_V_h = h1*(V11*h1 + V12*h2) + h2*(V21*h1 + V22*h2);
    double two_u_T_h = 2 * (u1*h1 + u2*h2);
    double g_h = h_T_V_h + two_u_T_h + f;
    
    // 3. Calculate m_T * (V*h + u)
    double Vh1 = V11*h1 + V12*h2;
    double Vh2 = V21*h1 + V22*h2;
    double m_T_Vh_plus_u = m1 * (Vh1 + u1) + m2 * (Vh2 + u2);

    // 4. Calculate the term under the square root
    double discriminant_term = m_T_Vh_plus_u * m_T_Vh_plus_u - g_h * m_T_V_m;

    if (discriminant_term >= 0 && m_T_V_m != 0) {
        double sqrt_discriminant = sqrt(discriminant_term);
        *kappa1 = (-m_T_Vh_plus_u + sqrt_discriminant) / m_T_V_m;
        *kappa2 = (-m_T_Vh_plus_u - sqrt_discriminant) / m_T_V_m;
    } else {
        *kappa1 = NAN;
        *kappa2 = NAN;
    }
}


