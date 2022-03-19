/* Write a C program to compute the perimeter and area of a circle with a given radius. Go to the editor
Expected Output:
Perimeter of the Circle = 37.680000 inches
Area of the Circle = 113.040001 square inches */

#include<stdio.h>
int main() {
  int radius = 6;
  
  printf("Perimeter of the Circle = %f inches\n", 2*3.14*radius);
  printf("Area of the Circle = %f square inches\n", 3.14*radius*radius);

  return 0;
}