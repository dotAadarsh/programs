// Replace all occurances of a character with another character.

#include<stdio.h>

int input(char str[]) {
  int ch, i=0;
  while((ch = getchar()) != '\n') {
    str[i++] = ch;
  }
  str[i] = '\0';
  return i;
}

void replace(char str[], char ch1, char ch2, int n) {
  for(int i=0;i<n;i++) {
    if(str[i]==ch1) {
      str[i] = ch2;
    }
  }
  printf("%s", str);
}

int main() {
  char str[100];
  int n= input(str);
  char ch1, ch2;
  scanf("%c %c", &ch1, &ch2);
  replace(str, ch1, ch2, n);
  return 0;
}