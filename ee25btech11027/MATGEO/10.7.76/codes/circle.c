#include <math.h>

/*
 * Calculates the number of common tangents between two circles.
 *
 * @param x1, y1, r1: Center coordinates and radius of the first circle.
 * @param x2, y2, r2: Center coordinates and radius of the second circle.
 * @return: Integer representing the number of common tangents.
 * - 4: Circles are separate.
 * - 3: Circles touch externally.
 * - 2: Circles intersect at two points.
 * - 1: Circles touch internally.
 * - 0: One circle is contained within the other.
 * - -1: Circles are concentric and identical (infinite tangents).
 */
int find_common_tangents(double x1, double y1, double r1, double x2, double y2, double r2) {
    // Calculate the distance between the centers
    double d = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));

    // Calculate the sum and difference of the radii
    double r_sum = r1 + r2;
    double r_diff = fabs(r1 - r2);

    // Determine the relationship between the circles
    if (d > r_sum) {
        return 4; // Circles are separate and do not intersect
    } else if (d == r_sum) {
        return 3; // Circles touch externally
    } else if (d > r_diff && d < r_sum) {
        return 2; // Circles intersect at two points
    } else if (d == r_diff) {
        return 1; // Circles touch internally
    } else if (d < r_diff) {
        return 0; // One circle is completely inside the other
    } else if (d == 0 && r1 == r2) {
        return -1; // Concentric and identical
    }

    return 0; // Default case, including d=0 and r1!=r2
}
