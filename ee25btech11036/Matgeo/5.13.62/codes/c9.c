
#include <stdint.h>

int get_count(void) {
    int count = 0;
    // There are 9 entries; treat them as base-3 digits 0,1,2
    for (int mask = 0; mask < 19683; ++mask) { // 3^9 = 19683
        int tmp = mask;
        int sumsq = 0;
        for (int i = 0; i < 9; ++i) {
            int digit = tmp % 3; // 0,1,2
            tmp /= 3;
            sumsq += digit*digit;
            if (sumsq > 5) break; // small optimization
        }
        if (sumsq == 5) ++count;
    }
    return count;
}
