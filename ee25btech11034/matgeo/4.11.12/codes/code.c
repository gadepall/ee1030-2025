#include <stdio.h>
#include <math.h>

// Define a structure to hold 3D point coordinates
typedef struct {
    double x;
    double y;
    double z;
} Point3D;

// --- Core Calculation Function ---
// Calculates the intersection point Q, the original point P, and the distance between them.
// The "__declspec(dllexport)" keyword ensures this function is exported from the DLL.
#ifdef _WIN32
    #define EXPORT __declspec(dllexport)
#else
    #define EXPORT
#endif
 __declspec(dllexport) double get_intersection_and_distance(Point3D* p_point, Point3D* q_point) {
    // Point P from the problem
    p_point->x = -1;
    p_point->y = -5;
    p_point->z = -10;

    // Line components: r = a + lambda * b
    Point3D a = {2, -1, 2};
    Point3D b = {3, 4, 2};

    // Plane normal vector: n
    Point3D n = {1, -1, 1};
    double d = 5.0;

    // --- Solve for lambda ---
    // (a + lambda*b) . n = d  =>  a.n + lambda*(b.n) = d
    double a_dot_n = a.x * n.x + a.y * n.y + a.z * n.z;
    double b_dot_n = b.x * n.x + b.y * n.y + b.z * n.z;
    
    // Handle division by zero case, although b_dot_n is 1 in this problem
    if (b_dot_n == 0) { 
        // Line is parallel to the plane, no unique intersection
        q_point->x = NAN; q_point->y = NAN; q_point->z = NAN;
        return -1.0;
    }
    double lambda = (d - a_dot_n) / b_dot_n;

    // --- Find Intersection Point Q ---
    q_point->x = a.x + lambda * b.x;
    q_point->y = a.y + lambda * b.y;
    q_point->z = a.z + lambda * b.z;

    // --- Calculate Distance between P and Q ---
    double dist_x = q_point->x - p_point->x;
    double dist_y = q_point->y - p_point->y;
    double dist_z = q_point->z - p_point->z;
    
    return sqrt(dist_x * dist_x + dist_y * dist_y + dist_z * dist_z);
}

// --- Point Generation for Plotting ---

// Generates points along the line for plotting
// The "__declspec(dllexport)" keyword ensures this function is exported from the DLL.
__declspec(dllexport) void generate_line_points(Point3D* points, int num_points) {
    Point3D a = {2, -1, 2};
    Point3D b = {3, 4, 2};
    for (int i = 0; i < num_points; ++i) {
        // Generate points for lambda from -2 to 2 for a good visualization
        double lambda = -2.0 + 4.0 * i / (num_points - 1);
        points[i].x = a.x + lambda * b.x;
        points[i].y = a.y + lambda * b.y;
        points[i].z = a.z + lambda * b.z;
    }
}

// Generates a grid of points on the plane for plotting
// The "__declspec(dllexport)" keyword ensures this function is exported from the DLL.
__declspec(dllexport) void generate_plane_points(Point3D* points, int grid_size, double range) {
    int index = 0;
    // The plane equation is x - y + z = 5, which we rearrange to z = 5 - x + y
    for (int i = 0; i < grid_size; ++i) {
        for (int j = 0; j < grid_size; ++j) {
            // Generate x and y coordinates over a specified range
            double x = -range + (2 * range * i) / (grid_size - 1);
            double y = -range + (2 * range * j) / (grid_size - 1);
            // Calculate z using the plane equation
            double z = 5.0 - x + y;
            points[index].x = x;
            points[index].y = y;
            points[index].z = z;
            index++;
        }
    }
}
