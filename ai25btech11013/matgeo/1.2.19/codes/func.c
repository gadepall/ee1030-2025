#include <stdio.h>

const char* check_quadrant(int x, int y) {
    if (x == 0 && y == 0) {
        return "Origin";
    } else if (x == 0) {
        return "Y-axis";
    } else if (y == 0) {
        return "X-axis";
    } else if (x > 0 && y > 0) {
        return "Quadrant I";
    } else if (x < 0 && y > 0) {
        return "Quadrant II";
    } else if (x < 0 && y < 0) {
        return "Quadrant III";
    } else {
        return "Quadrant IV";
    }
}
