//This program will not continue forever, however. The computer keeps function calls on a stack and once too many are called without ending, the program will crash. Why not write a program to see how many times the function is called before the program terminates?

#include<stdio.h>

void recurse(int n){
  printf("%d", n);
  recurse(n+1);
}

int main() {
  recurse(1);
  return 0;
  
}
