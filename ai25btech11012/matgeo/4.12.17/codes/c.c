#include <stdio.h>
#include <math.h>

int main() {
    double d = 5.0;  // given distance
    double x0, y0;   // intersection point
    double P1_x, P1_y, P2_x, P2_y;
    double Q1_x, Q1_y, Q2_x, Q2_y;
    double R1_x, R1_y, R2_x, R2_y;

    // Intersection of the two lines
    // Lines: y - sqrt(3)x = 2  and  y + sqrt(3)x = 2
    // Subtracting: -2sqrt(3)x = 0  => x=0, y=2
    x0 = 0.0;
    y0 = 2.0;

    // Direction vectors of the lines
    // For y - sqrt(3)x = 2, slope = sqrt(3), direction (1, sqrt(3))
    // For y + sqrt(3)x = 2, slope = -sqrt(3), direction (1, -sqrt(3))
    double dx1 = 1.0, dy1 = sqrt(3.0);
    double dx2 = 1.0, dy2 = -sqrt(3.0);

    // Normalize direction vectors
    double len1 = sqrt(dx1*dx1 + dy1*dy1);
    double len2 = sqrt(dx2*dx2 + dy2*dy2);

    dx1 /= len1; dy1 /= len1;
    dx2 /= len2; dy2 /= len2;

    // Points at distance d along each line from intersection
    P1_x = x0 + d*dx1;
    P1_y = y0 + d*dy1;

    P2_x = x0 + d*dx2;
    P2_y = y0 + d*dy2;

    // Angle bisectors are: x=0 (internal) and y=2 (external)

    // Feet of perpendiculars
    // On x=0 -> drop x-coordinate
    Q1_x = 0.0; Q1_y = P1_y;
    Q2_x = 0.0; Q2_y = P2_y;

    // On y=2 -> drop y-coordinate
    R1_x = P1_x; R1_y = 2.0;
    R2_x = P2_x; R2_y = 2.0;
    
    FILE* file;
	    file = fopen("values.dat","w");
    // Print results
    printf("Intersection point: (%.3f, %.3f)\n\n", x0, y0);

    fprintf(file,"P1 = (%.3f, %.3f)\n", P1_x, P1_y);
    fprintf(file,"P2 = (%.3f, %.3f)\n\n", P2_x, P2_y);

    fprintf(file,"Feet on internal bisector (x=0):\n");
    fprintf(file,"Q1 = (%.3f, %.3f)\n", Q1_x, Q1_y);
    fprintf(file,"Q2 = (%.3f, %.3f)\n\n", Q2_x, Q2_y);

    fprintf(file,"Feet on external bisector (y=2):\n");
    fprintf(file,"R1 = (%.3f, %.3f)\n", R1_x, R1_y);
    fprintf(file,"R2 = (%.3f, %.3f)\n", R2_x, R2_y);
     
    fclose(file);
    return 0;
}

