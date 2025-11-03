#include <stdio.h>
#include <math.h>

// Define PI if it's not available in math.h (M_PI is common but not standard)
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

int main() {
    // --- Given Parameters ---
    // Radius of the main circle C
    double radius = 3.0; 
    // Angle subtended by the chords at the center in radians
    double angle_rad = (2.0 * M_PI) / 3.0;

    // --- Calculation ---
    // The locus of the midpoints is another circle. Its radius (let's call it r_locus)
    // is found using the formula: r_locus = radius * cos(angle / 2).
    
    // 1. Find half the angle
    double half_angle = angle_rad / 2.0;

    // 2. Calculate the radius of the locus circle
    double locus_radius = radius * cos(half_angle);

    // 3. The equation of the locus is x^2 + y^2 = (locus_radius)^2.
    //    We need to find the value of the radius squared.
    double locus_radius_squared = pow(locus_radius, 2);

    // --- Output ---
    printf("Problem: Find the locus of the midpoints of chords of the circle x^2 + y^2 = %.0f\n", pow(radius, 2));
    printf("where the chords subtend an angle of 2*pi/3 at the center.\n\n");
    
    printf("--- Calculation Results ---\n");
    printf("Radius of the locus circle: %.2f\n", locus_radius);
    printf("Radius of the locus circle squared: %.2f\n\n", locus_radius_squared);

    printf("The final equation of the locus is: x^2 + y^2 = %.2f\n", locus_radius_squared);
    printf("This corresponds to option (d): x^2 + y^2 = 9/4\n");

    return 0;
}