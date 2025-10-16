    #include <stdio.h>
    #include <math.h>

    // Define a simple structure for a 2D point.
    struct Point {
        double x;
        double y;
    };

    // This function calculates the two tangent points (t1, t2) for a circle
    // centered at the origin with a given radius 'r', from an external point 'p'.
    // The results are returned via pointers.
    void calculate_tangents(double r, struct Point p, struct Point* t1, struct Point* t2) {
        // 1. Calculate the x-coordinate of the polar line.
        // This is where the line connecting the tangent points intersects the x-axis.
        double x_contact = (r * r) / p.x;

        // 2. Use the circle equation (x^2 + y^2 = r^2) to find the y-coordinates.
        double y_contact_sq = (r * r) - (x_contact * x_contact);

        // If y_contact_sq is negative, the point is inside the circle, and no tangents exist.
        if (y_contact_sq < 0) {
            // Set coordinates to NaN (Not a Number) to indicate an error.
            t1->x = t1->y = NAN;
            t2->x = t2->y = NAN;
            return;
        }

        double y_contact = sqrt(y_contact_sq);

        // 3. Assign the coordinates to the output structures.
        t1->x = x_contact;
        t1->y = y_contact;

        t2->x = x_contact;
        t2->y = -y_contact;
    }


    // Main function to demonstrate the tangent calculation for the specified problem.
    int main() {
        // Problem parameters: Circle radius 5, external point at (8, 0).
        double radius = 5.0;
        struct Point external_point = {8.0, 0.0};

        // Structures to hold the results.
        struct Point tangent_point1;
        struct Point tangent_point2;

        // Call the function to perform the calculation.
        calculate_tangents(radius, external_point, &tangent_point1, &tangent_point2);

        // Print the results.
        printf("Problem: Find tangents to a circle (radius=%.1f) from point (%.1f, %.1f)\n",
            radius, external_point.x, external_point.y);
        printf("----------------------------------------------------------------------\n");
        printf("Calculated Tangent Point 1 (T1): (%.4f, %.4f)\n", tangent_point1.x, tangent_point1.y);
        printf("Calculated Tangent Point 2 (T2): (%.4f, %.4f)\n", tangent_point2.x, tangent_point2.y);

        return 0;
    }


