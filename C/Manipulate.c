#include<stdio.h>
#include<string.h>

void strip_newline(char *str, int size) {
  int i;
  for(i=0;i<size;i++){
    if(str[i]=='\n'){
      str[i] = '\0';
      return;
    }
  }
}

int main(int argc, char *argv) {
  char name[50];
  char lastname[50];
  char fullname[100];

  printf("enter the name: ");
  fgets(name,50,stdin);
  strip_newline(name,50);

  if(strcmp(name,"madmax")==0){
    printf("Thats my name too \n");
  }
  else
    printf("Thats not my name\n");

  printf("Your name is %ld long\n", strlen(name));
  printf("Enter the last name: ");
  fgets(lastname,50, stdin);
  strip_newline(lastname,50);
  fullname[0]='\0';
  strcat(fullname, name);
  strcat(fullname, " ");
  strcat(fullname, lastname);

  printf("Your full name is : %s", fullname);

  getchar();
  return 0;
}