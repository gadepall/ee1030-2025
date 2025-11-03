#include <stdio.h>

// Function to compute cross product of two 3D vectors
void crossProduct(float a[3], float b[3], float result[3]) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}
int main() {
    // Define the two planes from the given question:
    // Plane 1: x + y + z = 1
    // Plane 2: 2x + 3y - z = -4
    
    float a1 = 1, b1 = 1, c1 = 1, d1 = 1;
    float a2 = 2, b2 = 3, c2 = -1, d2 = -4;

    float n1[3] = {a1, b1, c1};
    float n2[3] = {a2, b2, c2};

    // Step 1: Get direction vector of line of intersection
    float dir[3];
    crossProduct(n1, n2, dir);

    // Step 2: Find a point on the line of intersection
    // Let x = 0, then solve:
    // y + z = 1     => Equation A
    // 3y - z = -4   => Equation B

    float y, z;
    float det = b1 * c2 - b2 * c1; // b1*c2 - b2*c1 = 1*(-1) - 3*1 = -1 - 3 = -4

    if (det == 0) {
        printf("Determinant is zero, can't solve for unique point.\n");
        return 1;
    }

    y = (d1 * c2 - d2 * c1) / det;
    z = (b1 * d2 - b2 * d1) / det;
    float point[3] = {0, y, z};

    // Step 3: Since plane is parallel to X-axis, take vector (1, 0, 0)
    float xAxis[3] = {1, 0, 0};

    // Step 4: Cross product of dir and xAxis gives normal of required plane
    float normal[3];
    crossProduct(dir, xAxis, normal);

    // Step 5: Compute D in plane equation: ax + by + cz + d = 0
    float d = -(normal[0]*point[0] + normal[1]*point[1] + normal[2]*point[2]);
    printf("Equation of the required plane:\n");
    printf("%.2fx + %.2fy + %.2fz + %.2f = 0\n",
           normal[0], normal[1], normal[2], d);
return 0;
}
