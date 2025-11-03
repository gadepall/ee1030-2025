#include <stdio.h>

typedef struct {
    double x;
    double y;
} Point;

// Function to find third vertex given two vertices and orthocenter
Point third_vertex(double x1, double y1, double x2, double y2, double hx, double hy){
    Point C;
    double m_alt_A, m_alt_B;
    double m_perp_BC, m_perp_AC;

    // Slope of altitude from A passing through H
    if(x1 != hx)
        m_alt_A = (hy - y1)/(hx - x1);
    else
        m_alt_A = 1e9; // vertical slope

    // Slope of altitude from B passing through H
    if(x2 != hx)
        m_alt_B = (hy - y2)/(hx - x2);
    else
        m_alt_B = 1e9;

    // Equation for perpendicular slope relation
    if(m_alt_A != 1e9)
        m_perp_BC = -1.0 / m_alt_A;
    else
        m_perp_BC = 0; // horizontal BC

    if(m_alt_B != 1e9)
        m_perp_AC = -1.0 / m_alt_B;
    else
        m_perp_AC = 0; // horizontal AC

    // Solve system: slope formula
    // y3 - y2 = m_perp_BC * (x3 - x2)
    // y3 - y1 = m_perp_AC * (x3 - x1)
    double x3 = (m_perp_BC * x2 - m_perp_AC * x1 + y1 - y2) / (m_perp_BC - m_perp_AC);
    double y3 = m_perp_BC * (x3 - x2) + y2;

    C.x = x3;
    C.y = y3;
    return C;
}



