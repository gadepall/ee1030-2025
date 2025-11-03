#include <stdio.h>

int main() {
    int narayan_age, daughter_age;
    int solution_found = 0;

    // Let's iterate through possible ages.
    // We assume Narayan is older than his daughter.
    for (narayan_age = 1; narayan_age <= 150; narayan_age++) {
        for (daughter_age = 1; daughter_age < narayan_age; daughter_age++) {

            // Condition 1: Seven years ago, Narayan was 7 times his daughter's age.
            // (narayan_age - 7) == 7 * (daughter_age - 7)
            int is_condition1_met = (narayan_age - 7) == 7 * (daughter_age - 7);

            // Condition 2: Three years from now, Narayan will be 3 times his daughter's age.
            // (narayan_age + 3) == 3 * (daughter_age + 3)
            int is_condition2_met = (narayan_age + 3) == 3 * (daughter_age + 3);

            // If both conditions are true, we've found the answer.
            if (is_condition1_met && is_condition2_met) {
                printf("Solution Found:\n");
                printf("Narayan's current age is: %d\n", narayan_age);
                printf("Daughter's current age is: %d\n", daughter_age);
                
                solution_found = 1;
                break; // Exit the inner loop
            }
        }
        if (solution_found) {
            break; // Exit the outer loop
        }
    }

    if (!solution_found) {
        printf("No solution found within the specified age range.\n");
    }
    return 0;
}