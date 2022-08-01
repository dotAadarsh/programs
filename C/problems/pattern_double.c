#include<stdio.h>
#include<math.h>
#include <stdlib.h>

void pattern(int n){
  int count = 1;
  for(int i=0;i<2*n-1;i++) {
    for(int j=0;j<abs(n-i-1);j++) 
      printf(" ");
    for(int j=0;j<2*(n-abs(n-i-1))-1;j++)
      printf("%d", count++);
    printf("\n");
  }
}

int main() {
  int n;
  scanf("%d", &n);
  pattern(n);
  return 0;
}