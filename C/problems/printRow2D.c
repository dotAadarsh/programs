// Write a program to print the given two dimensionl data on row wise traversal

#include<stdio.h>
int main() {
  
  int row, col;
  scanf("%d %d", &row, &col);
  
  long int arr[row][col];
  
  for(int i=0;i<row;i++) {
    for(int j=0;j<col;j++) {
      
      scanf("%ld", &arr[i][j]);
    }
  }

  for(int i=0;i<row;i++) {
    for(int j=0;j<col;j++) {
      printf("%ld ", arr[i][j]);
    } 
    printf("\n");
  }
  
  return 0;
}