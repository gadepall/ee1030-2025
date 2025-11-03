#include <stdio.h>
#include <math.h>

// A structure to represent a point in 2D space
struct Point {
    double x;
    double y;
};

// Function to calculate the circumcenter (center of the Apollonian circle)
struct Point findCircumcenter(struct Point p1, struct Point p2, double ratio) {
    struct Point center;
    double k = ratio;
    double k_squared = k * k;

    // Formula for the center of the Circle of Apollonius
    // Center (h, k) = ( (x1 - k^2*x2) / (1 - k^2), (y1 - k^2*y2) / (1 - k^2) )
    center.x = (p1.x - k_squared * p2.x) / (1 - k_squared);
    center.y = (p1.y - k_squared * p2.y) / (1 - k_squared);

    return center;
}

int main() {
    // Define the two fixed points from the problem
    struct Point p1 = {1.0, 0.0};  // Point (1, 0)
    struct Point p2 = {-1.0, 0.0}; // Point (-1, 0)

    // Define the given ratio
    double ratio = 1.0 / 3.0;

    // Calculate the circumcenter
    struct Point circumcenter = findCircumcenter(p1, p2, ratio);

    // Print the result
    printf("The circumcenter of the triangle ABC is at the point: (%.2f, %.2f)\n",
           circumcenter.x, circumcenter.y);

    printf("In fraction form, this is (5/4, 0).\n");

    return 0;
}