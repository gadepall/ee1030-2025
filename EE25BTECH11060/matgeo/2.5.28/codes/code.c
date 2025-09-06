#include <stdio.h>

int main() {
    
    double a[3] = {2, 3, 2};
    double b[3] = {2, 2, 1};
    double dot = 0.0, normB2 = 0.0;

    for(int i = 0; i < 3; i++) {
        dot += a[i] * b[i];
        normB2 += b[i] * b[i];
    }

    
    double factor = dot / normB2;

    
    double proj[3];
    for(int i = 0; i < 3; i++) {
        proj[i] = factor * b[i];
    }

    
    printf("Projection of a on b = (%.2lf)i + (%.2lf)j + (%.2lf)k\n",
           proj[0], proj[1], proj[2]);

    return 0;
}
