#include<stdio.h>
int main(int argc, char *argv[]) {
  int i=0;

  if(argc == 1) {
    printf("You ony have one argument\n");
  }
  else if(argc>1&&argc<4) {
    printf("Heres your argument: \n");
      for(i=0;i<argc;i++){
        printf("%s ",argv[i]);
      }
    printf(" \n");
  }else{
    printf("No arguments\n");
  }
  return 0;
}