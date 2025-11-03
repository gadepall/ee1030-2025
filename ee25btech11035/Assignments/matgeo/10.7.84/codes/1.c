#include<stdio.h>
#include <math.h>

double calculateOALength(double radius, double m1_x, double m1_y, double m2_x, double m2_y) {
    // 1. Calculate the cosine of the angle (2*phi) between the tangents
    double dot_product = m1_x * m2_x + m1_y * m2_y;
    double norm_m1 = sqrt(m1_x * m1_x + m1_y * m1_y);
    double norm_m2 = sqrt(m2_x * m2_x + m2_y * m2_y);
    double cos_2_phi = dot_product / (norm_m1 * norm_m2);

    // 2. Use the half-angle identity for tangent: tan^2(phi) = (1 - cos(2*phi)) / (1 + cos(2*phi))
    double tan_phi_squared = (1.0 - cos_2_phi) / (1.0 + cos_2_phi);
    double tan_phi = sqrt(tan_phi_squared);

    // 3. The length of OA is radius / tan(phi)
    double oa_length = radius / tan_phi;

    return oa_length;
}