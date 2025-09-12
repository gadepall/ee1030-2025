#include <stdio.h>
#include <math.h>

int main() {
    double D[3] = {2.0, 2.0, 3.0};
    double mag = sqrt(D[0]*D[0] + D[1]*D[1] + D[2]*D[2]);

    printf("Magnitude: %.5f\n", mag);
    printf("Direction Cosines:\n");
    for (int i = 0; i < 3; i++) {
        printf("%.5f\n", D[i]/mag);
    }
    return 0;
}
