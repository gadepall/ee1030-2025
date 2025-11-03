#include <math.h>
#include <stdlib.h>

// Structure to hold intersection points
typedef struct {
    double x1, y1;
    double x2, y2;
} Intersection;

Intersection solve_conic(double p) {
    Intersection result;

    // Solve x^2 + px - (3p^2)/4 = 0
    double a = 1.0;
    double b = p;
    double c = -0.75 * p * p;

    double discriminant = b * b - 4 * a * c;
    if (discriminant < 0) {
        result.x1 = result.y1 = result.x2 = result.y2 = NAN;
        return result;
    }

    double sqrt_d = sqrt(discriminant);
    double x1 = (-b + sqrt_d) / (2 * a);
    double x2 = (-b - sqrt_d) / (2 * a);

    // y^2 = 2px ⇒ y = ±sqrt(2px)
    double y1 = sqrt(2 * p * x1);
    double y2 = -y1;

    result.x1 = x1;
    result.y1 = y1;
    result.x2 = x1;
    result.y2 = y2;

    return result;
}

