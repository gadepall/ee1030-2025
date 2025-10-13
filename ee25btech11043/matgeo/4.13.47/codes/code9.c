#include <math.h>

// Function to calculate the foot of the perpendicular from point P to line segment AB
// P_x, P_y: coordinates of point P
// A_x, A_y: coordinates of point A
// B_x, B_y: coordinates of point B
// foot_x, foot_y: pointers to store the calculated coordinates of the foot of the perpendicular
void calculateFootOfPerpendicular(double P_x, double P_y,
                                  double A_x, double A_y,
                                  double B_x, double B_y,
                                  double *foot_x, double *foot_y) {
    // Vector AB
    double BA_x = B_x - A_x;
    double BA_y = B_y - A_y;

    // Vector AP
    double AP_x = P_x - A_x;
    double AP_y = P_y - A_y;

    // Calculate lambda using the projection formula:
    // lambda = (AP . AB) / |AB|^2
    double dot_product_AP_BA = AP_x * BA_x + AP_y * BA_y;
    double length_sq_BA = BA_x * BA_x + BA_y * BA_y;

    double lambda = dot_product_AP_BA / length_sq_BA;

    // The foot of the perpendicular F lies on the line AB:
    // F = A + lambda * (B - A)
    *foot_x = A_x + lambda * BA_x;
    *foot_y = A_y + lambda * BA_y;
}