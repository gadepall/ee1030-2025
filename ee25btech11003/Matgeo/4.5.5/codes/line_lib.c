#include <stdio.h>

/**
 * @brief Prints the parametric equations of a 3D line.
 * This function is designed to be compiled into a shared library (.so or .dll)
 * and called from other languages like Python.
 */
void printParametricForm(double px, double py, double pz, double vi, double vj, double vk) {
    printf("--- Output from C Function ---\n");
    printf("Parametric Equations for the line:\n");
    printf("  x = %.2f %+g*t\n", px, vi);
    printf("  y = %.2f %+g*t\n", py, vj);
    printf("  z = %.2f %+g*t\n", pz, vk);
    printf("------------------------------\n\n");
}

