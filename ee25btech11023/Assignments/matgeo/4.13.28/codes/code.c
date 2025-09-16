
#include <math.h>

void calculate_slope_data(double* out_data) {
    double px = 2.0, py = 3.0;
     
    // Solve the quadratic equation for x using the quadratic formula
    double a = 1.0, b = -6.0, c = 2.0;
    double discriminant = sqrt(b*b - 4*a*c);
    
    // Find the two possible x-coordinates for the intersection points
    double q1_x = (-b + discriminant) / (2 * a); // 3 + sqrt(7)
    double q2_x = (-b - discriminant) / (2 * a); // 3 - sqrt(7)

    // Find the corresponding y-coordinates using y = 7 - x
    double q1_y = 7 - q1_x;  
    double q2_y = 7 - q2_x;  
    
    // Calculate the two possible slopes m = (y_q - y_p) / (x_q - x_p)
    double slope1 = (q1_y - py) / (q1_x - px);
    double slope2 = (q2_y - py) / (q2_x - px);

    out_data[0] = px;      out_data[1] = py;
    out_data[2] = q1_x;    out_data[3] = q1_y;
    out_data[4] = q2_x;    out_data[5] = q2_y;
    out_data[6] = slope1;  out_data[7] = slope2;
}