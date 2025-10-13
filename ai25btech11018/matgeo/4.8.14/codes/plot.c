#include <stdio.h>
#include <math.h>

int main() {
  
    double p[3] = {2.0, 3.0, 1.0};
    double n[3] = {2.0, 1.0, 3.0};
    double d0 = 26.0;

    // --- 1. Perpendicular Distance ---
    
   
    double dot_product_pn = 0.0;
    for (int i = 0; i < 3; i++) {
        dot_product_pn += p[i] * n[i];
    }

 double magnitude_n_sq = 0.0;
    for (int i = 0; i < 3; i++) {
        magnitude_n_sq += n[i] * n[i];
    }
    double magnitude_n = sqrt(magnitude_n_sq);

   
    double distance = fabs(dot_product_pn - d0) / magnitude_n;
    printf("Perpendicular Distance: %.2f / %.2f = %.4f\n\n", fabs(dot_product_pn - d0), magnitude_n, distance);

    // --- 2. Foot of Perpendicular ---
    double scalar_factor = (dot_product_pn - d0) / magnitude_n_sq;
    double q[3];

for (int i = 0; i < 3; i++) {
        q[i] = p[i] - scalar_factor * n[i];
    }
    printf("Position vector of Foot of Perpendicular (Q):\n");
    printf("(%.4f, %.4f, %.4f)\n\n", q[0], q[1], q[2]);

    // --- 3. Image of P ---
    double p_prime[3];
    for (int i = 0; i < 3; i++) {
        p_prime[i] = 2.0 * q[i] - p[i];
    }
    printf("Position vector of Image of P (P'):\n");
    printf("(%.4f, %.4f, %.4f)\n\n", p_prime[0], p_prime[1], p_prime[2]);
    return 0;
}
