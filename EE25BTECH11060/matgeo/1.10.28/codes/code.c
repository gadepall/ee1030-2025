#include <stdio.h>
#include <math.h>
int main() {
    double angle = 30.0;
    double angle_rad = angle * M_PI / 180.0;
    double x_component = cos(angle_rad);
    double y_component = sin(angle_rad);
    printf("Unit vector in the XY plane making a 30 degree angle with the X-axis: \n");
    printf("r = %.2f i + %.2f j\n", x_component, y_component);
    return 0;
}
