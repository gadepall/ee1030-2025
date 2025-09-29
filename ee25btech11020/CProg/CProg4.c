//Code by Darsh Gajare
//August 18, 2025
//Drawing bar graph and finding max and min
#include <stdio.h>
#include <stdlib.h>
#include "datafun.h"
#define MAX_HEIGHT 10
// declaring function
void printBarGraph(char *colours[], int students[], int n);
void bar(int val, int thresh);
void compare(char *colours[], int students[], int n);
// main function
int main()
{
	char *colours[] = {"Red", "Green", "Blue", "Yellow", "Orange"};
	int students[] = {43, 19, 55, 49, 34};
	int n=5;
	printBarGraph(colours,students,n);
	compare(colours, students, n);
	return 0;
}
void compare(char *colours[], int students[], int n)
{
	int max,min=0;
	for(int i=0; i<n; i++)
	{
		if(students[i]>students[max])
			max=i;
		if(students[i]<students[min])
			min=i;
	}
	printf("Most preferred colour is %s\n",colours[max]);
	printf("Least preferred colour is %s\n",colours[min]);
	printf("%d is the total number of colours\n",n);
	for(int i=0; i<n; i++)
	printf("%s ",colours[i]);
	printf("\n");
}
void printBarGraph(char *colours[], int students[], int n)
{
	//Find maximum value
	int l=max(students,n);
	//bar graph scaling factor
	float scale=(l>MAX_HEIGHT)?(float)MAX_HEIGHT/l :1.0;
	//Draw the bars vertically
	for(int row=MAX_HEIGHT; row>0 ; row--)
	{
		for (int i=0;i<n;i++)
		{
			printf(" ");
			bar((int)(students[i]*scale),row);
		}
		printf("\n");
	}
	//draw X-axis
	for(int i=0;i<n;i++)
	{
		printf("---");
	}
	printf("\n");
	//show your labels
	for(int i=0;i<n;i++)
	{
		printf("%s ",colours[i]);
	}
	printf("\n");
}
//drawing bars
void bar(int val, int thresh)
{
	if(val>=thresh)
		printf("| ");
	else
		printf("  ");
}
