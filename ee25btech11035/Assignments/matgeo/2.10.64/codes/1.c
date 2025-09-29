#include <stdio.h>
#include <math.h> // Required for NAN (Not a Number)

/**
 * @brief Represents a point or vector in 3D space.
 */
typedef struct {
    double x;
    double y;
    double z;
} Point3D;

/**
 * @brief Specifies which coordinate (X, Y, or Z) is the unknown.
 */
typedef enum {
    UNKNOWN_X,
    UNKNOWN_Y,
    UNKNOWN_Z
} UnknownCoord;

/**
 * @brief Calculates a missing coordinate, given four points must be coplanar.
 * @details Solves for the unknown by ensuring the scalar triple product of the
 * vectors (B-A), (C-A), and (D-A) is zero. The resulting linear
 * equation is solved for the unknown coordinate.
 *
 * @param pA Pointer to the first point (A).
 * @param pB Pointer to the second point (B).
 * @param pC Pointer to the third point (C).
 * @param pD Pointer to the fourth point (D).
 * @param unknown_point_index Index of the point with the missing value (0=A, 1=B, 2=C, 3=D).
 * @param unknown_coord_axis Enum specifying the unknown axis (X, Y, or Z).
 *
 * @return The calculated value for the missing coordinate. Returns NAN if no unique solution exists.
 */
double solve_coplanar_coord(Point3D pA, Point3D pB, Point3D pC, Point3D pD, 
                            int unknown_point_index, UnknownCoord unknown_coord_axis) {

    // Array of pointers for easy access to the points by index.
    Point3D* points[] = {&pA, &pB, &pC, &pD};
    Point3D* unknown_point = points[unknown_point_index];

    // Helper function to calculate the determinant of the three vectors formed from the points.
    double calculate_determinant(Point3D a, Point3D b, Point3D c, Point3D d) {
        // Form vectors relative to point A
        double ab_x = b.x - a.x; double ab_y = b.y - a.y; double ab_z = b.z - a.z;
        double ac_x = c.x - a.x; double ac_y = c.y - a.y; double ac_z = c.z - a.z;
        double ad_x = d.x - a.x; double ad_y = d.y - a.y; double ad_z = d.z - a.z;

        // Calculate the determinant of the matrix [AB, AC, AD]
        return ab_x * (ac_y * ad_z - ac_z * ad_y) -
               ab_y * (ac_x * ad_z - ac_z * ad_x) +
               ab_z * (ac_x * ad_y - ac_y * ad_x);
    }

    // Solve the linear equation `a*lambda + b = 0` for the unknown `lambda`.

    // 1. Calculate 'b' by setting the unknown coordinate to 0.
    double original_value;
    switch(unknown_coord_axis) {
        case UNKNOWN_X: original_value = unknown_point->x; unknown_point->x = 0.0; break;
        case UNKNOWN_Y: original_value = unknown_point->y; unknown_point->y = 0.0; break;
        case UNKNOWN_Z: original_value = unknown_point->z; unknown_point->z = 0.0; break;
    }
    double b = calculate_determinant(pA, pB, pC, pD);

    // 2. Calculate 'a+b' by setting the unknown coordinate to 1.
    switch(unknown_coord_axis) {
        case UNKNOWN_X: unknown_point->x = 1.0; break;
        case UNKNOWN_Y: unknown_point->y = 1.0; break;
        case UNKNOWN_Z: unknown_point->z = 1.0; break;
    }
    double a_plus_b = calculate_determinant(pA, pB, pC, pD);

    // Restore the original value to the point struct to prevent side effects.
    switch(unknown_coord_axis) {
        case UNKNOWN_X: unknown_point->x = original_value; break;
        case UNKNOWN_Y: unknown_point->y = original_value; break;
        case UNKNOWN_Z: unknown_point->z = original_value; break;
    }
    
    // 3. Calculate 'a'.
    double a = a_plus_b - b;

    // If 'a' is near zero, a unique solution doesn't exist.
    if (fabs(a) < 1e-9) {
        return NAN;
    }

    // 4. Solve for the unknown: lambda = -b / a
    return -b / a;
}