#include <stdio.h>

// Structure for returning intersection
struct Point {
    float x;
    float y;
    float z;
};

// Function to compute intersection of diagonals
struct Point find_intersection() {
    // Coordinates of vertices
    float Px=4, Py=2, Pz=-6;
    float Qx=5, Qy=-3, Qz=1;
    float Rx=12, Ry=4, Rz=5;
    float Sx=11, Sy=9, Sz=-2;

    // Midpoints of diagonals
    struct Point O;
    O.x = (Px + Rx) / 2.0;
    O.y = (Py + Ry) / 2.0;
    O.z = (Pz + Rz) / 2.0;

    return O;
}

// Function to print equations of diagonals
void print_equations() {
    float Px=4, Py=2, Pz=-6;
    float Qx=5, Qy=-3, Qz=1;
    float Rx=12, Ry=4, Rz=5;
    float Sx=11, Sy=9, Sz=-2;

    printf("Equation of diagonal PR: (x,y,z) = (%.1f, %.1f, %.1f) + t(%.1f, %.1f, %.1f)\\n",
           Px, Py, Pz, Rx-Px, Ry-Py, Rz-Pz);

    printf("Equation of diagonal QS: (x,y,z) = (%.1f, %.1f, %.1f) + s(%.1f, %.1f, %.1f)\\n",
           Qx, Qy, Qz, Sx-Qx, Sy-Qy, Sz-Qz);
}