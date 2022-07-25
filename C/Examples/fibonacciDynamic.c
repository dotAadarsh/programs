// https://dzone.com/articles/what-is-dynamic-programming

#include<stdio.h>

int fibonacci(int n) {
  int result = 0;
  if(n == 1 || n == 2) {
    return 1;
  }
  // used to store previous two results
  int lastButOneValue = 1;
  int lastValue = 1;  
  // Work from item 3

  for(int i=3;i<=n;i++) {
    result = lastValue  + lastButOneValue;
    // Update the values of the previous two items in the sequence
    lastButOneValue=lastValue;
    lastValue = result;
  }
  return result;
}
int main() {
  int n;
  scanf("%d", &n);
  printf("%d", fibonacci(n));
  return 0;
}