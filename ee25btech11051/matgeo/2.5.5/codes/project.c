#include <stddef.h>
#include<math.h>

void project(double* result, const double* arr2, const double* arr3, int length) {
    float dot_product = 0.0f;
    float magnitude_squared = 0.0f;
    
    for (int i = 0; i < length; i++) {
        dot_product += arr2[i] * arr3[i];
    }

    
    for (int i = 0; i < length; i++) {
        magnitude_squared += arr3[i] * arr3[i];
    }

    
    if (magnitude_squared == 0.0f) {
        for (int i = 0; i < length; i++) {
            result[i] = 0.0f;
        }
        return;
    }

    
    const float scalar = dot_product / magnitude_squared;

    
    for (int i = 0; i < length; i++) {
        result[i] = scalar * arr3[i];
    }

    for(int i=0; i<length; i++){
	result[i] = floor(result[i] * 100) / 100;   /* Result: 37.77 */
    }
}
