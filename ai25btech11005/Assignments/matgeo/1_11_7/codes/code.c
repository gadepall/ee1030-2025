#include <stdio.h>
2 #include <math.h>
3 int main() {
4 double a = -18, b = 12, c = -4;
5 double magnitude;
6 double l, m, n;
7 // Calculate magnitude of the vector
8 magnitude = sqrt(a * a + b * b + c * c);
9 // Calculate direction cosines
0 l = a / magnitude;
1 m = b / magnitude;
2 n = c / magnitude;
3 // Print direction cosines
4 printf("Direction cosines are:\n");
5 printf("l = %.6f\n", l);
6 printf("m = %.6f\n", m);
7 printf("n = %.6f\n", n);
8 return 0;
9 }Megha Shyam-AI25BTECH11005 1.11.7 september 26,2025 4 / 6
Python Plotting Code - Part 1