#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main()
{
    double horizontal = 10.0;
    double vertical = 30.0;

    double theta_rad = atan(horizontal / vertical);
    double theta_deg = theta_rad * 180.0 / M_PI;

    // Print to screen (like before)
    printf("Horizontal component (north) = %.1f m/s,\n", horizontal);
    printf("Vertical component (down) = %.1f m/s.\n\n", vertical);
    printf("tan(theta) = %.1f / %.1f = %.2f\n", horizontal, vertical, horizontal / vertical);
    printf("theta = arctan(%.2f) ≈ %.2f degrees\n\n", horizontal / vertical, theta_deg);
    printf("Conclusion: In her frame the rain comes from slightly ahead (from the south and above),\n");
    printf("so she should tilt the umbrella forward (toward the direction of motion, i.e., south)\n");
    printf("by %.2f degrees from the vertical.\n", theta_deg);

    // Also write results into a file like the second program
    FILE *file;
    file = fopen("values.dat", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "horizontal\tvertical\ttheta_deg\n");
    fprintf(file, "%.1f\t%.1f\t%.2f\n", horizontal, vertical, theta_deg);

    fclose(file);
    printf("Results have been written to values.dat\n");

    return 0; 
}

