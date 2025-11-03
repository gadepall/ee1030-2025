#include <stdio.h>
#include <math.h> // Required for the square root function sqrt()

int main() {
    // Coefficients for the quadratic equation: x^2 - 55x + 750 = 0
    double a = 1.0;
    double b = -55.0;
    double c = 750.0;

    double discriminant, root1, root2;

    // Calculate the discriminant (b^2 - 4ac)
    discriminant = b * b - 4 * a * c;

    // Check if real solutions exist
    if (discriminant >= 0) {
        // Calculate the two possible roots using the quadratic formula
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);

        printf("The problem translates to the quadratic equation: x^2 - 55x + 750 = 0\n");
        printf("Solving for x, we find two possible solutions.\n\n");
        
        // Print the final answer in the context of the problem
        printf("The number of toys produced on that day was either %.0f or %.0f.\n\n", root1, root2);
        
        // Verification for both cases
        printf("Verification:\n");
        printf("Case 1: If %.0f toys were produced, the cost per toy is (55 - %.0f) = %.0f. Total cost = %.0f * %.0f = %.0f\n", root1, root1, (55-root1), root1, (55-root1), root1*(55-root1));
        printf("Case 2: If %.0f toys were produced, the cost per toy is (55 - %.0f) = %.0f. Total cost = %.0f * %.0f = %.0f\n", root2, root2, (55-root2), root2, (55-root2), root2*(55-root2));

    } else {
        // This case will not occur for the given problem numbers
        printf("The equation has no real solutions, which means there is an error in the problem's premises.\n");
    }
    return 0;
}