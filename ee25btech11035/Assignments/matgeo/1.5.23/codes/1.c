#include <stdio.h>
#include<math.h>

int areCollinear3D(int x1, int y1, int z1,
                   int x2, int y2, int z2,
                   int x3, int y3, int z3) {
    int ABx = x2 - x1, ABy = y2 - y1, ABz = z2 - z1;
    int ACx = x3 - x1, ACy = y3 - y1, ACz = z3 - z1;

    int crossX = ABy * ACz - ABz * ACy;
    int crossY = ABz * ACx - ABx * ACz;
    int crossZ = ABx * ACy - ABy * ACx;

    if (crossX == 0 && crossY == 0 && crossZ == 0)
        return 1; // Collinear
    else
        return 0; // Not collinear
}
