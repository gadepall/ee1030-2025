#include <stdio.h>

int main() {
    // Data from the table
    char *students[] = {"Ajay", "Bali", "Dipti", "Falgun", "Geetika", "Hari"};
    int marks[] = {450, 500, 300, 360, 400, 540};
    int num_students = sizeof(marks) / sizeof(marks[0]);
    int max_mark = 600; // Total marks out of 600

    printf("Bar Graph of Marks Obtained:\n\n");

    // Find the maximum mark obtained to scale the graph (optional, but good for relative representation)
    // For this example, we'll just use the given marks directly for bar length
    // You could also scale them to fit a certain console width

    for (int i = 0; i < num_students; i++) {
        printf("%-8s | ", students[i]); // Print student name, left-aligned in 8 chars
        // Print the bar using '*' characters, scaled to a reasonable length
        // Here, we'll use a simple scaling: 10 marks = 1 '*'
        for (int j = 0; j < marks[i] / 10; j++) {
            printf("*");
        }
        printf(" %d\n", marks[i]); // Print the actual mark
    }

    printf("\nNote: Each '*' represents 10 marks.\n");

    return 0;
}
