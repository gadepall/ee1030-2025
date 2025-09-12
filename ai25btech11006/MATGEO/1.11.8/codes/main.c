#include <stdio.h>
#include <math.h>

int main() {
    // Coordinates of points P and Q
    float Px = 4, Py = 3, Pz = -5;
    float Qx = -2, Qy = 1, Qz = -8;
    
    // Direction vector PQ = Q - P
    float dx = Qx - Px;
    float dy = Qy - Py;
    float dz = Qz - Pz;
    
    // Magnitude of PQ
    float magnitude = sqrt(dx*dx + dy*dy + dz*dz);
    
    // Direction cosines (unit vector components)
    float l = dx / magnitude;
    float m = dy / magnitude;
    float n = dz / magnitude;
    
    // Output the result
    printf("Direction Cosines: (%.3f, %.3f, %.3f)\n", l, m, n);
    
    return 0;
}

