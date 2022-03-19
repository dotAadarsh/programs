#include<stdio.h>
int main(int argc, char* argv[]) {
  
  int var = 10;
  int* pointee = &var;
  int a,b;

  printf("pointee stors the address of var:  %p\n",pointee);
  printf("Value in pointee is %d\n", *pointee);
  printf("The address of a and b is %p and %p", &a,&b);

  return 0;
}