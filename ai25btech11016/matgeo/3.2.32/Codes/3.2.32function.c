#include <stdio.h>

// Function to fill the coordinates of A, B, C
// coords must be a double array of size 6
// Format: [Ax, Ay, Bx, By, Cx, Cy]
void get_triangle_coords(double *coords) {
    // Right triangle with B at (0,0), C on x-axis, A on y-axis
    coords[0] = 0.0;  // A.x
    coords[1] = 5.0;  // A.y
    coords[2] = 0.0;  // B.x
    coords[3] = 0.0;  // B.y
    coords[4] = 12.0; // C.x
    coords[5] = 0.0;  // C.y
}