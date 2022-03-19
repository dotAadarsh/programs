/*
Write a C program to get the C version you are using. Go to the editor
Expected Output ex:
We are using C18!
*/

#include<stdio.h>
int main(int argc, char** argv[]) {
  
  #if __STDC_VERSION__ >= 201710L
  printf("We are using C18!\N");
  #elif __STDC_VERSION__ >= 201112L
  printf("We are using C11!\n");
  #elif __STDC_VERSION__ >= 19901L
  printf("We are using C99");
  #else
  printf("We are using C89/C90!\n");
  #endif
  
  return 0;
}
