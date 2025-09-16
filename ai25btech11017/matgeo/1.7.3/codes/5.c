#include <stdio.h>

int main() {
    // Points A, B, C
    int Ax = -2, Ay = 3, Az = 5;
    int Bx =  1, By = 2, Bz = 3;
    int Cx =  7, Cy = 0, Cz = -1;

    // Vectors AB = B - A, AC = C - A
    int ABx = Bx - Ax;
    int ABy = By - Ay;
    int ABz = Bz - Az;

    int ACx = Cx - Ax;
    int ACy = Cy - Ay;
    int ACz = Cz - Az;

    printf("Vector AB = (%d, %d, %d)\n", ABx, ABy, ABz);
    printf("Vector AC = (%d, %d, %d)\n", ACx, ACy, ACz);

    // Check if AC is a scalar multiple of AB
    // (Cross product must be zero for collinearity)
    int cross_x = ABy * ACz - ABz * ACy;
    int cross_y = ABz * ACx - ABx * ACz;
    int cross_z = ABx * ACy - ABy * ACx;

    printf("Cross product AB x AC = (%d, %d, %d)\n", cross_x, cross_y, cross_z);

    if (cross_x == 0 && cross_y == 0 && cross_z == 0) {
        printf("✅ Points A, B, and C are collinear.\n");
    } else {
        printf("❌ Points A, B, and C are NOT collinear.\n");
    }

    return 0;
}

