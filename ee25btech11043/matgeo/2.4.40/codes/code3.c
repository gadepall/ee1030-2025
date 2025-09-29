#include <stdio.h>
#include <math.h>

// Function to calculate the angle between two lines in degrees
// given their slopes m1 and m2
void findAngleBetweenLines(double m1, double m2, double *angle_degrees) {
    // Calculate the tangent of the angle
    double tan_theta = (m1 - m2) / (1 + m1 * m2);

    // Calculate the angle in radians using atan
    double angle_radians = atan(tan_theta);

    // Convert the angle from radians to degrees
    *angle_degrees = angle_radians * (180.0 / M_PI);

    // Ensure the angle is positive
    if (*angle_degrees < 0) {
        *angle_degrees += 180.0;
    }
}

int main() {
    double m1, m2;        // Slopes of the two lines
    double calculated_angle_degrees; // Variable to store the calculated angle

   

    // Call the function to calculate the angle
    findAngleBetweenLines(m1, m2, &calculated_angle_degrees);

    // The angle is now stored in 'calculated_angle_degrees'.
    
    return 0;
}