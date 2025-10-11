#include <stdio.h>
#include <math.h>

int main(void) {
    /* Given point P */
    double Px = 0.0, Py = 1.0, Pz = 2.0;

    /* X-axis is all points (t, 0, 0). 
       The perpendicular foot Q from P to the X-axis is (Px, 0, 0). */
    double Qx = Px;
    double Qy = 0.0;
    double Qz = 0.0;

    /* (Optional) distance from P to the X-axis */
    double distance = sqrt(Py*Py + Pz*Pz);

    printf("Point P: (%.2f, %.2f, %.2f)\n", Px, Py, Pz);
    printf("Foot of perpendicular on X-axis, Q: (%.2f, %.2f, %.2f)\n", Qx, Qy, Qz);
    printf("Distance from P to X-axis: %.2f\n", distance);

    return 0;
}
