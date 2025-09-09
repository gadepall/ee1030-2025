#include <stdio.h>

// Function to calculate point C of rectangle
// A=(Ax,Ay), B=(Bx,By), D=(Dx,Dy)
// Returns Cx and Cy via pointers
void findC(float Ax, float Ay, float Bx, float By, float Dx, float Dy, float *Cx, float *Cy) {
    *Cx = Bx + Dx - Ax;
    *Cy = By + Dy - Ay;
}
