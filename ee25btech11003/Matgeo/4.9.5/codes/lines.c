
#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

// Define an export macro for cross-platform compatibility (for Windows DLLs)
#ifdef _WIN32
   #define EXPORT __declspec(dllexport)
#else
   #define EXPORT
#endif

EXPORT void calculate_rotated_lines(double a, double b, double px, double py, double angle_deg,
                                    double *a1, double *b1, double *c1,
                                    double *a2, double *b2, double *c2) {
    double m_orig_x = -b;
    double m_orig_y = a;
    double angle_rad = angle_deg * M_PI / 180.0;
    double cos_angle = cos(angle_rad);
    double sin_angle = sin(angle_rad);

    double m1_x = m_orig_x * cos_angle - m_orig_y * sin_angle;
    double m1_y = m_orig_x * sin_angle + m_orig_y * cos_angle;
    double m2_x = m_orig_x * cos_angle + m_orig_y * sin_angle;
    double m2_y = -m_orig_x * sin_angle + m_orig_y * cos_angle;

    *a1 = -m1_y;
    *b1 = m1_x;
    *c1 = (*a1) * px + (*b1) * py;
    *a2 = -m2_y;
    *b2 = m2_x;
    *c2 = (*a2) * px + (*b2) * py;
}
