#include <stdio.h>

// Function to check if triangle is right-angled
// Returns 1 if right-angled, 0 otherwise
int is_right_triangle() {
    // Vertices
    float Ax = -4, Ay = 0;
    float Bx = 0,  By = 3;
    float Cx = 4,  Cy = 0;

    // Side vectors
    float AB[2] = {Ax - Bx, Ay - By};
    float BC[2] = {Bx - Cx, By - Cy};
    float AC[2] = {Ax - Cx, Ay - Cy};

    // Dot products
    float dot1 = AB[0]*BC[0] + AB[1]*BC[1];
    float dot2 = BC[0]*AC[0] + BC[1]*AC[1];
    float dot3 = AC[0]*AB[0] + AC[1]*AB[1];

    if (dot1 == 0 || dot2 == 0 || dot3 == 0)
        return 1;   // Right-angled
    else
        return 0;   // Not right-angled
}

// Function to check if triangle is isosceles
// Returns 1 if isosceles, 0 otherwise
int is_isosceles() {
    // Vertices
    float Ax = -4, Ay = 0;
    float Bx = 0,  By = 3;
    float Cx = 4,  Cy = 0;

    // Midpoints of sides
    float x_mid[2] = {(Ax + Bx) / 2, (Ay + By) / 2};
    float y_mid[2] = {(Bx + Cx) / 2, (By + Cy) / 2};
    float z_mid[2] = {(Ax + Cx) / 2, (Ay + Cy) / 2};

    // Medians
    float median1[2] = {x_mid[0] - Cx, x_mid[1] - Cy};
    float median2[2] = {y_mid[0] - Ax, y_mid[1] - Ay};
    float median3[2] = {z_mid[0] - Bx, z_mid[1] - By};

    // Side vectors
    float AB[2] = {Ax - Bx, Ay - By};
    float BC[2] = {Bx - Cx, By - Cy};
    float AC[2] = {Ax - Cx, Ay - Cy};

    // Dot products (median ⟂ opposite side ?)
    float dot1 = median1[0]*AB[0] + median1[1]*AB[1];
    float dot2 = median2[0]*BC[0] + median2[1]*BC[1];
    float dot3 = median3[0]*AC[0] + median3[1]*AC[1];

    if (dot1 == 0 || dot2 == 0 || dot3 == 0)
        return 1;  // Isosceles
    else
        return 0;  // Not isosceles
}
