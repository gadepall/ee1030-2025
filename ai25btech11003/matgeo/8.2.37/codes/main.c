#include <stdio.h>

/*
  Compute parameters for the parabola with:
    Vertex (h,k) = (–3,0)
    Directrix    = x + 5 = 0  =>  x = –5
  Write to main.dat:
    h, k, p, focus_x, focus_y, directrix_x
*/

int main() {
    double h = -3.0, k = 0.0;
    double directrix_x = -5.0;
    // p = (h - directrix_x) / 2  (distance/2; opens right)
    double p = (h - directrix_x) / 2.0;
    double focus_x = h + p;
    double focus_y = k;

    FILE *fp = fopen("main.dat", "w");
    if (!fp) {
        perror("Unable to open main.dat");
        return 1;
    }
    fprintf(fp, "%f %f %f %f %f %f\n",
            h, k, p, focus_x, focus_y, directrix_x);
    fclose(fp);
    return 0;
}

