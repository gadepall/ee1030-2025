#include <stdio.h>

// Function to compute a point on the line
// Params: (px, py, pz) = point on line
//         (dx, dy, dz) = direction vector
//         t            = parameter
// Output: coords[3] = coordinates of point
void line_point(float px, float py, float pz,
                float dx, float dy, float dz,
                float t, float coords[3]) {
    coords[0] = px + dx * t;  // x = x0 + t*dx
    coords[1] = py + dy * t;  // y = y0 + t*dy
    coords[2] = pz + dz * t;  // z = z0 + t*dz
}
