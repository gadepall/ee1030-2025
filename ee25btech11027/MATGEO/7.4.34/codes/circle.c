#include <math.h>

typedef struct {
    double x;
    double y;
} Point;

void solve_circle_tangency(double G1, double H1, double K1, Point p, double r2, Point* c1_center_out, Point* c2_center_out) {
    double c1_x = -G1 / 2.0;
    double c1_y = -H1 / 2.0;
    double m_x = p.x - c1_x;
    double m_y = p.y - c1_y;
    double mag_m = sqrt(m_x * m_x + m_y * m_y);
    double m_hat_x = m_x / mag_m;
    double m_hat_y = m_y / mag_m;
    c1_center_out->x = c1_x;
    c1_center_out->y = c1_y;
    c2_center_out->x = p.x + r2 * m_hat_x;
    c2_center_out->y = p.y + r2 * m_hat_y;
}
