#include <stdio.h>

int are_collinear(float A[3], float B[3], float C[3]) {
    float AB[3], AC[3];

    for (int i = 0; i < 3; i++) {
        AB[i] = B[i] - A[i];
        AC[i] = C[i] - A[i];
    }

    float ratio = 0.0;
    int initialized = 0;
        for (int i = 0; i < 3; i++) {
        if (AC[i] != 0) {
            float current_ratio = AB[i] / AC[i];
            if (!initialized) {
                ratio = current_ratio;
                initialized = 1;
            } else {
                if (current_ratio != ratio) {
                    return 0; 
                }
            }
        } else if (AB[i] != 0) {
            return 0; 
        }
    }

    return 1; 
}
