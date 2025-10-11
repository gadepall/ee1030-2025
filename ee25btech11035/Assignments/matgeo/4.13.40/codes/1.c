#include <stdio.h>

// Function to count integer values of m for which intersection x is integer
int count_integer_m(int a1, int b1, int c1, int m_min, int m_max) {
    int count = 0;

    for(int m = m_min; m <= m_max; m++) {
        int a2 = -m;   // From y = mx + 1 -> -m*x + 1*y = 1
        int b2 = 1;
        int c2 = 1;

        int det = a1 * b2 - a2 * b1;   // denominator
        if(det == 0) continue;         // parallel or coincident → skip

        int num_x = c1 * b2 - b1 * c2; // numerator for x

        if(num_x % det == 0) {         // x is integer
            count++;
        }
    }

    return count;
}