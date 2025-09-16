#include <stdio.h>

int main() {
    // The problem statement is:
    // The scalar product of vector 'a' with the unit vector along the sum of vectors 'b' and 'c' is equal to one.
    // Vector a = i + j + k
    // Vector b = 2i + 4j - 5k
    // Vector c = λi + 2j + 3k

    // Step 1: Find the sum vector, s = b + c
    // s = (2+λ)i + (4+2)j + (-5+3)k
    // s = (2+λ)i + 6j - 2k

    // Step 2: The given condition is a · (s / |s|) = 1, which simplifies to a · s = |s|.
    
    // Step 3: Calculate the dot product a · s
    // a · s = (1 * (2+λ)) + (1 * 6) + (1 * -2) = 2 + λ + 6 - 2 = λ + 6

    // Step 4: Find the magnitude squared, |s|^2
    // |s|^2 = (2+λ)^2 + 6^2 + (-2)^2 = (2+λ)^2 + 36 + 4 = (2+λ)^2 + 40

    // Step 5: Set up the equation (a · s)^2 = |s|^2
    // (λ + 6)^2 = (2+λ)^2 + 40

    // Step 6: Expand and simplify the equation
    // λ^2 + 12λ + 36 = (λ^2 + 4λ + 4) + 40
    // λ^2 + 12λ + 36 = λ^2 + 4λ + 44
    // 12λ - 4λ = 44 - 36
    // 8λ = 8

    // Step 7: Solve for λ
    float coefficient_of_lambda = 8.0;
    float constant = 8.0;
    float lambda = constant / coefficient_of_lambda;

    // Display the final result
    printf("The problem simplifies to the linear equation: 8 * lambda = 8\n");
    printf("Solving for lambda...\n");
    printf("The value of lambda is: %.0f\n", lambda);

   return 0;
}