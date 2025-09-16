#include <stdio.h>
#include <math.h>

int main() {
    // Given values
    double boat_speed = 25.0;       // km/h towards North
    double current_speed = 10.0;    // km/h at 60° east of South
    double angle = 60.0 * M_PI / 180.0; // Convert degrees to radians

    // Resolve the current into components
    // North-South axis (Y-axis): South is negative, North is positive
    double current_y = -current_speed * cos(angle);
    // East-West axis (X-axis): East is positive
    double current_x = current_speed * sin(angle);

    // Boat velocity components (boat is moving North)
    double boat_x = 0.0;
    double boat_y = boat_speed;

    // Resultant components
    double resultant_x = boat_x + current_x;
    double resultant_y = boat_y + current_y;

    // Calculate magnitude and direction
    double resultant_speed = sqrt(resultant_x * resultant_x +
                                  resultant_y * resultant_y);

    // atan2(x, y) gives angle east of north in radians → convert to degrees
    double resultant_angle = atan2(resultant_x, resultant_y) * 180.0 / M_PI;

    // Output
    printf("Resultant Velocity: %.2f km/h\n", resultant_speed);
    printf("Direction: %.2f degrees east of north\n", resultant_angle);

    return 0;
}

