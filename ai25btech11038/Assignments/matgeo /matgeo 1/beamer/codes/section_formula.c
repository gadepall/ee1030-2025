#include <stdio.h>
#include <math.h>
float dotProduct(float a[3], float b[3]) { return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]; 
} 
float normSquared(float a[3]) { 
return dotProduct(a, a); 
}
float findK(float P[3], float Q[3], float R[3]) { 
float QP[3], RP[3]; 
for (int i = 0; i < 3; i++) { QP[i] = Q[i] - P[i]; RP[i] = R[i] - P[i]; } float numerator = dotProduct(QP, RP);
float denominator = normSquared(RP);
if (denominator == 0) {
return 0.0f; // if P and R are same point, k is undefined return 0 
} 
return numerator / denominator;
}