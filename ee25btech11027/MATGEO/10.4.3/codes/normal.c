

#include <math.h>
void solve_for_point(double line_A, double line_B, double* contact_x, double* contact_y) {
    // Slope of the given line
    double m_line = -line_A / line_B;

    // Slope of the normal to the curve (which is perpendicular to the line)
    double m_normal_req = -1.0 / m_line;
    
    
    double x_squared = m_normal_req / (1.0 + m_normal_req);
    
    double x = sqrt(x_squared); // Taking positive root since x > 0
    double y = x + (1.0 / x);
    
    // Store the results in the output pointers
    *contact_x = x;
    *contact_y = y;
}
