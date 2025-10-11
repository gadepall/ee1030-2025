#include <stdio.h>
#include <math.h>

void get_results(double *out_data) {
    
    double side = 2.0;
    double r1 = side / 2.0;          
    double r2 = side / sqrt(2.0);    

    
    double ratio = (r1 * r1 + r1 * r1 + r1 * r1 + r1 * r1) /
                   (r2 * r2 + r2 * r2 + r2 * r2 + r2 * r2);

    
    double k = 2.0;
    double focus_x = 0.0;
    double focus_y = k + r1;
    double directrix_y = k - r1;

   
    double area = 2.0 / 3.0;

    double a = 1;
    double b = -1;
    out_data[0] = ratio;
    out_data[1] = focus_x;
    out_data[2] = focus_y;
    out_data[3] = directrix_y;
    out_data[4] = area;
    out_data[5] = a; //Ax
    out_data[6] = a; //Ay
    out_data[7] = b; //Bx
    out_data[8] = a; //By
    out_data[9] = b; //Cx
    out_data[10] = b; //Cy
    out_data[11] = a; //Dx
    out_data[12] = b; //Dy
    out_data[13] = 0.5; //T1x
    out_data[14] = 0.5; //T1y;
    out_data[15] = 0; //T2x;
    out_data[16] = 2; //T2y
    out_data[17] = 2; //T3x
    out_data[18] = 0; //T3y 

}
