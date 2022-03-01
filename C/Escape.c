//Escape Sequences

#include<stdio.h>
int main(int argc, char *argv[])

{
  printf("backslash a - Alert (Beep, Bell) \a \n");
  printf("backslash b - Backspace\b\n");
  printf("\ebackslash e -  Escape character\n");
  printf("backslash e - \f Form Feed\n");
  printf("backslash n - \n New Line\n");
  printf("backslash r - \r Carriage return\n");
  printf("backslash t - \t 	Tab (Horizontal)\n");
  printf("backslash v - \v 	Vertical Tab\n");
  printf("backslash backslash - \\ Backslash\n");
  printf("backslash ' - \' Single Quote\n");
  printf(" \n\"baba blacksheep example\" ");
  printf("backslash ? - \? Question Mark\n");
  printf("backslash nnn - \123 	octal number\n");
  printf("backslash xhh - \x5b hexadecimal number\n");
    
}