#include <stdio.h>

int main() {
    int a, b, c, d;
    int count = 0;

    // Each entry can be 1, 2, or 3
    for (a = 1; a <= 3; a++) {
        for (b = 1; b <= 3; b++) {
            for (c = 1; c <= 3; c++) {
                for (d = 1; d <= 3; d++) {
                    count++;
                    printf("Matrix %d:\n", count);
                    printf("%d %d\n", a, b);
                    printf("%d %d\n\n", c, d);
                }
            }
        }
    }

    printf("Total matrices = %d\n", count);
    return 0;
}




