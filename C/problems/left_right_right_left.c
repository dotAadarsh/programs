// Write a program to print the given two dimensionl data on Left-Right_Right-Left traversal

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
  if(i%2==0) {
    for(int j=0;j<col;j++) {
      printf("%ld ", arr[i][j]);
    }
    printf("\n");
  }
  else {
    for(int j=col-1;j>=0;j--) {
      printf("%ld ", arr[i][j]);
    }
    printf("\n");
  }
}
  return 0;
}