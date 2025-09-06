#include <stdio.h>

int main() {
    float M[2][3] = {
        {-1, -5, 7},
        {1, 5, -7}
    };

    for (int i = 0; i < 3; i++)
        M[1][i] += M[0][i];

    if (M[1][0] == 0 && M[1][1] == 0 && M[1][2] == 0)
        printf("Rank = 1\nPoints are collinear\n");
    else
        printf("Rank > 1\nPoints are not collinear\n");

    return 0;
}
